from fpqs import *

def u_f(circuit, num_qubits):
    """Implement an oracle returning TRUE if all the digits of the input are 1 (i.e. 111111 is the only solution) 

        Parameters:
        circuit (QuantumCircuit): the quantum circuit on the oracle which operates
        num_qubits (int): Number of qubits
    """
    circuit.mcx(list(range(6)), 6)


# Run the simulation
def simulate_fpqs_circ(n_shots=100, auto_iter = True, num_iter=None, num_qubit=6, plot=True):
    target = QuantumRegister(6)
    ancilla = QuantumRegister(1)
    A = QuantumCircuit(target, ancilla)

    A.h(target)
    
    fp_qc = fpqs_circ(u_f, .5, num_qubit, A, 6, target, num_iter)
    
    A.append(fp_qc, range(0, len(A.qubits)))
    A.measure_all()

    print(A)

    fpqs_qc_transpiled = transpile(A, Aer.get_backend('aer_simulator'))

    result = AerSimulator().run(fpqs_qc_transpiled, shots=n_shots, memory=True).result()
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

simulate_fpqs_circ()