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


# def u_f(circuit, num_qubits):
#     """Implement an oracle returning TRUE if the first two digits of the input are 11 (e.g. 1100 is a solution, 0100 is not) 

#         Parameters:
#         circuit (QuantumCircuit): the quantum circuit on the oracle which operates
#         num_qubits (int): Number of qubits
#     """

#     circuit.ccx(0, 1, num_qubits)


def u_f(circuit, num_qubits):
    """Implement an oracle returning TRUE if all the digits of the input are 1 (i.e. 111111 is the only solution) 

        Parameters:
        circuit (QuantumCircuit): the quantum circuit on the oracle which operates
        num_qubits (int): Number of qubits
    """
    circuit.mcx(list(range(6)), 6)

def s_beta(beta, num_qubits):
    """Implement the S(\beta) operator

    Parameters:
        beta (float): angle
        num_qubits (int): Number of qubits

    Returns:
        QuantumCircuit: Quantum circuit representing S(\beta)
    """

    # Create the quantum circuit
    # print(num_qubits)
    circuit = QuantumCircuit(num_qubits + 1, name="S(\beta)")

    # Apply U_f to all qubits
    u_f(circuit, num_qubits)

    # Apply Z_beta to ancilla qubit
    circuit.rz(beta,num_qubits)
    
    # Apply U_f to all qubits
    u_f(circuit, num_qubits)

    return circuit    


def s_alpha(alpha, num_qubits):
    """Implement the S(\alpha) operator

    Parameters:
        alpha (float): angle
        num_qubits (int): Number of qubits

    Returns:
        QuantumCircuit: Quantum circuit representing W(\alpha)
    """
    
    # Create quantum circuit
    circuit = QuantumCircuit(num_qubits + 1, name="W(\alpha)")

    # Apply A_dagger to all num_qubits qubits
    circuit.barrier()
    circuit.h(range(num_qubits))             # A_dagger = A, since H is self-adjoint
    circuit.barrier()

    # Apply Z_{-alpha0.5} to last qubit (not ancilla qubit)
    circuit.barrier()
    circuit.rz(-alpha*0.5,num_qubits-1) 
    circuit.barrier()

    # Apply Multi-(XoX)-controlled NOT gate to last and ancilla qubit
    circuit.barrier()
    circuit.x(range(num_qubits-1))
    circuit.barrier()
    circuit.mcx(list(range(num_qubits-1)), num_qubits-1)
    circuit.barrier()
    circuit.mcx(list(range(num_qubits-1)), num_qubits)
    circuit.barrier()
    circuit.x(range(num_qubits-1))
    circuit.barrier()

    # Apply Z_{-alpha0.5} to last qubit AND ancilla qubit
    circuit.rz(-alpha*0.5,num_qubits-1) 
    circuit.barrier()
    circuit.rz(-alpha*0.5,num_qubits) 
    circuit.barrier()

    # Apply Multi-(XoX)-controlled CNOT gate to last and ancilla qubit
    circuit.x(range(num_qubits-1))
    circuit.barrier()
    circuit.mcx(list(range(num_qubits-1)), num_qubits-1)
    circuit.barrier()
    circuit.mcx(list(range(num_qubits-1)), num_qubits)
    circuit.barrier()
    circuit.x(range(num_qubits-1))
    circuit.barrier()

    # Apply Z_alpha to last qubit (not ancilla qubit)
    circuit.rz(alpha,num_qubits-1) 
    circuit.barrier()

    # Apply A to all num_qubits qubits
    circuit.h(range(num_qubits)) 
    circuit.barrier() 

    return circuit


def fpqs_circ(delta, num_qubits, auto_num_step = True, num_steps=0):
    """Implement G(alpha, beta)

    Parameters:
        delta (float): Precision parameter in (0,1]
        num_qubits (int): Number of qubits
        auto_num_step (bool): default to True, refers to who should decide the number of steps 
        num_steps (int): Number of steps of the algorithm (l), by default decided by the system

    Returns:
        QuantumCircuit: Quantum circuit G(alpha, beta) with input state preparation
    """

    # Computing the number of stemps assuming the worst case scenario (M = 1)
    if auto_num_step == True:
        num_steps = int(np.ceil(np.log(2/delta)*np.sqrt(np.power(2, num_qubits))))

    print(num_steps)
    # Compute the number of qubits in circuit
    qc = QuantumCircuit(num_qubits + 1)

    # Prepare input state
    qc.h(list(range(num_qubits)))

    # Run the generalized Grover iterator for num_steps times
    for j in range(num_steps):
        alpha = alpha_fixed_point(j + 1, num_steps, delta)      # Compute \alpha_j
        beta = beta_fixed_point(j + 1, num_steps, delta)        # Compute \beta_j
        qc.compose(s_beta(beta, num_qubits), inplace=True)      # S(\beta_j)
        qc.compose(s_alpha(alpha, num_qubits), inplace=True)    # S(\alpha_j)
    
    return qc


# Run the simulation
def simultare_fpqs_circ(n_shots=100, auto_iter = True, num_iter=None, num_qubit=4, plot=True):
    fp_qc = fpqs_circ(.5, num_qubit, auto_iter, num_iter)
    fp_qc.measure_all()

    print(fp_qc)

    result = AerSimulator().run(fp_qc, shots=n_shots, memory=True).result()
    counts = result.get_counts()

    if plot == True:
        plt.figure(figsize=(10, 5))
        plt.bar(counts.keys(), counts.values())
        plt.xlabel('States')
        plt.ylabel('Frequency')
        plt.xticks(rotation=90)
        plt.tight_layout()
        plt.show()

    print(counts)
    return counts

# simultare_fpqs_circ()