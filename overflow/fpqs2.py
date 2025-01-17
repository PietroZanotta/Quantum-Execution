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


def s_beta(beta, num_qubits, oracle, digits):
    """
        Implement the S(\beta) operator

        Parameters:
            beta (float): angle
            num_qubits (int): Number of qubits
            oracle (function): Oracle function of the circuit
            digits (int): number of digits representing the numbers in the circuit

        Returns:
            QuantumCircuit: Quantum circuit representing S(\beta)
    """

    # Initialization
    circuit = QuantumCircuit(num_qubits+1, digits, name="S(\beta)")
    
    # Apply the oracle to all qubits
    oracle(circuit)

    # Apply Z_beta to ancilla qubit
    circuit.barrier()
    circuit.barrier()
    circuit.barrier()
    circuit.barrier()
    circuit.barrier()

    circuit.rz(beta,num_qubits)

    circuit.barrier()
    circuit.barrier()
    circuit.barrier()
    circuit.barrier()
    circuit.barrier()
    
    # Apply the oracle to all qubits
    oracle(circuit)

    return circuit    


def s_alpha(alpha, num_qubits, A):
    """Implement the S(\alpha) operator

    Parameters:
        alpha (float): angle
        num_qubits (int): Number of qubits
        A (function): function preparing the search space

    Returns:
        QuantumCircuit: Quantum circuit representing S(\alpha)
    """
    
   # Initialization
    num_qubits = 4
    n_qubits = 15
    digits = 4

    circuit = QuantumCircuit(n_qubits, 4, name="W(\alpha)")
    
    # Apply A_dagger to all num_qubits qubits
    circuit.barrier()
    A(circuit)
    circuit.barrier()

    # Apply Z_{-alpha0.5} to last qubit (not ancilla qubit)
    circuit.barrier()
    circuit.rz(-alpha*0.5,num_qubits-1) 
    circuit.barrier()

    # Apply Multi-(XoX)-controlled NOT gate to last and ancilla qubit
    circuit.x(range(0, num_qubits-1)) 
    circuit.mcx([0,1,2], num_qubits-1) 
    circuit.mcx([0,1,2], 14)
    circuit.x(range(0, num_qubits-1)) 

    # Apply Z_{-alpha0.5} to last qubit AND ancilla qubit
    circuit.barrier()
    circuit.rz(-alpha*0.5,num_qubits-1) 
    circuit.rz(-alpha*0.5,14)    
    circuit.barrier()

    # Apply Multi-(XoX)-controlled CNOT gate to last and ancilla qubit
    circuit.x(range(num_qubits-1)) 
    circuit.barrier()
    circuit.mcx([0,1,2], num_qubits-1) 
    circuit.barrier()
    circuit.mcx([0,1,2], 14)
    circuit.barrier()
    circuit.x(range(num_qubits-1)) 
    circuit.barrier()

    # Apply Z_alpha to last qubit (not ancilla qubit)
    circuit.rz(alpha,num_qubits-1) 
    circuit.barrier()

    # Apply A to all num_qubits qubits
    circuit.barrier()
    A(circuit)
    circuit.barrier()

    return circuit


def fpqs_circ(oracle, delta, num_qubits, digits, A, num_steps=None):
    """Implement G(alpha, beta)

    Parameters:
        oracle (func): Oracle function for the circuit (U)
        delta (float): Precision parameter in (0,1]
        num_qubits (int): Number of qubits on which the fpqs is running
        digits (int): number of digits representing the numbers in the circuit 
        A (function): function preparing the search space
        num_steps (int): Number of steps of the algorithm (l). If none, the number of steps is automatically selected

    Returns:
        QuantumCircuit: Quantum circuit G(alpha, beta) with input state preparation
    """

    # Computing the number of steps assuming the worst case scenario (M = 1)
    if num_steps == None:
        num_steps = int(np.ceil(np.log(2/delta)*np.sqrt(np.power(2, digits))))

    print(num_steps)


    # Compute the number of qubits in circuit
    qc = QuantumCircuit(3*digits + 3, digits, name="fpqs")

    # Prepare input state
    A(qc)

    # num_qubits = len(qc.qubits)-1
    num_qubits = num_qubits-1

    # Run the generalized Grover iterator for num_steps times
    for j in range(num_steps):
        alpha = alpha_fixed_point(j + 1, num_steps, delta)      # Compute \alpha_j
        beta = beta_fixed_point(j + 1, num_steps, delta)        # Compute \beta_j
        qc.compose(s_beta(beta, num_qubits, oracle, digits), inplace=True) # S(\beta_j)
        qc.barrier()      
        qc.append(s_alpha(alpha, num_qubits, A), range(0, 15), range(0,4))    # S(\alpha_j)
        qc.barrier()      
    
    return qc

