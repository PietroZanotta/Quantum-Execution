import math
import numpy as np
from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
from qiskit_aer import AerSimulator


def acot(x):
    return math.atan2(1, x)    


def cheb(i, x):
    return math.cosh(i * math.acosh(x))


def gamma(L, delta):
    return 1./cheb(1./L, 1./delta)


def alpha_fixed_point(j, l, delta):
    L = 2 * l + 1
    return 2 * acot(math.tan(2 * math.pi * j/L) * math.sqrt(1 - gamma(L, delta)**2))


def beta_fixed_point(j, l, delta):
    return -alpha_fixed_point(l - j + 1, l, delta)


def s_beta(beta, num_qubits, oracle):
    """
        Implement the S(\beta) operator

        Parameters:
            beta (float): angle
            num_qubits (int): Number of qubits
            oracle (function): Oracle function of the circuit

        Returns:
            QuantumCircuit: Quantum circuit representing S(\beta)
    """

    # Create the quantum circuit
    circuit = QuantumCircuit(num_qubits + 1, name="S(\beta)")

    # Apply the oracle to all qubits
    circuit.barrier()
    oracle(circuit, num_qubits)
    circuit.barrier()

    # Apply Z_beta to ancilla qubit
    circuit.rz(beta,num_qubits)
    
    # Apply the oracle to all qubits
    oracle(circuit, num_qubits)

    return circuit    


def s_alpha(alpha, num_qubits, A):
    """
        Implement the S(\alpha) operator

        Parameters:
            alpha (float): angle
            num_qubits (int): Number of qubits
            A (QuantumCircuit): Quantum circuit to prepare the search space

        Returns:
            QuantumCircuit: Quantum circuit representing S(\alpha)
    """
    
    # Create quantum circuit
    circuit = QuantumCircuit(num_qubits + 1, 4, name="S(\alpha)")

    # Apply A_dagger 
    circuit.append(A.inverse(), range(num_qubits+1), range(0,4))        

    # Apply Z_{-alpha0.5} to last qubit (not ancilla qubit)
    circuit.rz(-alpha*0.5,num_qubits-2) 

    # Apply Multi-(XoX)-controlled NOT gate to last and ancilla qubit
    circuit.x(range(num_qubits-2))
    circuit.mcx(list(range(num_qubits-2)), num_qubits-2)
    circuit.mcx(list(range(num_qubits-2)), num_qubits)
    circuit.x(range(num_qubits-2))

    # Apply Z_{-alpha0.5} to last qubit AND ancilla qubit
    circuit.rz(-alpha*0.5,num_qubits-2) 
    circuit.rz(-alpha*0.5,num_qubits) 

    # Apply Multi-(XoX)-controlled CNOT gate to last and ancilla qubit
    circuit.x(range(num_qubits-2))
    circuit.mcx(list(range(num_qubits-2)), num_qubits-2)
    circuit.mcx(list(range(num_qubits-2)), num_qubits)
    circuit.x(range(num_qubits-2))

    # Apply Z_alpha to last qubit (not ancilla qubit)
    circuit.rz(alpha,num_qubits-2) 

    # Apply A to all num_qubits qubits
    circuit.append(A, range(num_qubits+1), range(0,4))   # !!!

    return circuit


def fpqs_circ(oracle, delta, n_qubits, A, num_steps=None):
    """
        Implement G(alpha, beta)

        Parameters:
            oracle (func): Oracle function for the circuit (U)
            delta (float): Precision parameter in (0,1]
            n_qubits (int): Number of qubits on which the fpqs is running
            A (QuantumCircuit): Quantum circuit preparing the search space
            num_steps (int): Number of steps of the algorithm (l). If none, the number of steps is automatically selected

        Returns:
            QuantumCircuit: Quantum circuit G(alpha, beta) with input state preparation
    """
    
    # Computing the number of stemps assuming the worst case scenario (M = 1)
    if num_steps == None:
        num_steps = int(np.ceil(np.log(2/delta)*np.sqrt(np.power(2, n_qubits))))

    print(num_steps)

    # Get the dimension of the circuit from A
    num_qubits = len(A.qubits) - 1

    # Compute the number of qubits in circuit
    qc = QuantumCircuit(num_qubits + 1, name="fpqs")

    # Run the generalized Grover iterator for num_steps times
    for j in range(num_steps):
        alpha = alpha_fixed_point(j + 1, num_steps, delta)      # Compute \alpha_j
        beta = beta_fixed_point(j + 1, num_steps, delta)        # Compute \beta_j
        qc.compose(s_beta(beta, num_qubits, oracle), inplace=True)      # S(\beta_j)
        qc.compose(s_alpha(alpha, num_qubits, A), inplace=True)    # S(\alpha_j)
    
    return qc
