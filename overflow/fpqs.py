import math
import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, transpile
import matplotlib.pyplot as plt
from qiskit_aer import AerSimulator, Aer


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


def s_beta(beta, num_qubits, oracle, ancilla, A):
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
    circuit = QuantumCircuit(A.qubits, name="S(\beta)")
    ancilla = circuit.qubits[ancilla]

    # Apply the oracle to all qubits
    circuit.barrier()
    oracle(circuit, num_qubits)
    circuit.barrier()

    # Apply Z_beta to ancilla qubit
    circuit.rz(beta, ancilla)
    
    # Apply the oracle to all qubits
    oracle(circuit, num_qubits)

    return circuit    


def s_alpha(alpha, num_qubits, A, target, ancilla):
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
    circuit = QuantumCircuit(A.qubits, name="S(\alpha)")
    ancilla = circuit.qubits[ancilla]
    # Apply A_dagger 
    circuit.append(A.inverse(), range(len(A.qubits)))  
    circuit.barrier()    
      

    # Apply Z_{-alpha0.5} to last qubit (not ancilla qubit)
    circuit.rz(-alpha*0.5, target[-2]) 
    circuit.barrier()    

    # Apply multicontrolled NOT gate to last and ancilla qubit
    circuit.x(A.qubits)
    circuit.x(target[-2])
    circuit.x(ancilla)
    circuit.barrier()    

    out = [target[-2]]
    out.extend([ancilla])

    contr = list(filter(lambda x: x not in out, A.qubits)) # All the qubits but the last target qubit and the ancilla 
    # print("\n\n")
    # print(len(contr))
    # print("\n\n")
    circuit.mcx(contr, target[-2])
    circuit.mcx(contr, ancilla)
    circuit.barrier()    

    circuit.x(ancilla)
    circuit.x(target[-2])
    circuit.x(A.qubits)
    circuit.barrier()    

    # Apply Z_{-alpha0.5} to last qubit AND ancilla qubit
    circuit.rz(-alpha*0.5, target[-2]) 
    circuit.rz(-alpha*0.5, ancilla) 
    circuit.barrier()    
   
    # Apply multicontrolled NOT gate to last and ancilla qubit
    circuit.x(A.qubits)
    circuit.x(target[-2])
    circuit.x(ancilla)
    circuit.barrier()    

    out = [target[-2]]
    out.extend([ancilla])
    contr = list(filter(lambda x: x not in out, A.qubits)) # All the qubits but the last target qubit and the ancilla 

    circuit.mcx(contr, target[-2])
    circuit.mcx(contr, ancilla)
    circuit.barrier()    

    circuit.x(ancilla)
    circuit.x(target[-2])
    circuit.x(A.qubits)
    circuit.barrier()    

    # Apply Z_alpha to last qubit (not ancilla qubit)
    circuit.rz(alpha, target[-2]) 
    circuit.barrier()    

    # Apply A to all qubits
    circuit.append(A, range(len(A.qubits))) 

    return circuit


def fpqs_circ(oracle, delta, n_qubits, A, ancilla, target, num_steps=None):
    """
        Implement G(alpha, beta), based on Theodore J. Yoder, Guang Hao Low, and Isaac L. Chuang, "Fixed-Point Quantum Search with an Optimal Number of Queries", (2014)

        Parameters:
            oracle (func): Oracle function for the circuit (U)
            delta (float): Precision parameter in (0,1]
            n_qubits (int): Number of qubits on which the fpqs is running (i.e. number of qubits of the solution)
            A (QuantumCircuit): Quantum circuit preparing the search space (should also include the ancilla)
            target ([Qubits]): a list of qubits representing the target
            num_steps (int): Number of steps of the algorithm (l). If none, the number of steps is automatically selected

        Returns:
            QuantumCircuit: Quantum circuit G(alpha, beta) with input state preparation

        Note:
            - The original quantum circuit should already include the ancilla
            - One has to append the output of this function to the main circuit
    """
    
    # Computing the number of stemps assuming the worst case scenario (M = 1)
    if num_steps == None:
        num_steps = int(np.ceil(np.log(2/delta)*np.sqrt(np.power(2, n_qubits))))

    print(num_steps)

    # Get the dimension of the circuit from A
    num_qubits = len(target)

    # Compute the number of qubits in circuit
    # print("\n\n")
    # print(type(ancilla))
    qc = QuantumCircuit(A.qubits, name="fpqs")

    # Run the generalized Grover iterator for num_steps times
    for j in range(num_steps):
        alpha = alpha_fixed_point(j + 1, num_steps, delta)      # Compute \alpha_j
        beta = beta_fixed_point(j + 1, num_steps, delta)        # Compute \beta_j
        qc.compose(s_beta(beta, num_qubits, oracle, ancilla, A), inplace=True)      # S(\beta_j)
        qc.barrier()    
        qc.compose(s_alpha(alpha, num_qubits, A, target, ancilla), inplace=True)    # S(\alpha_j)
        qc.barrier()    
    
    return qc