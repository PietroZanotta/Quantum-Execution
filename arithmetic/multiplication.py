import math
import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit.circuit.library import QFT, CU1Gate
import matplotlib.pyplot as plt
from qiskit_aer import AerSimulator, Aer

def preparation(a_bin, b_bin):
    # Encoding a and b into quantum states
    num_qubits = len(a_bin) + len(b_bin)
    circuit = QuantumCircuit(num_qubits + 1)

    print(b_bin)
    for i in range(len(b_bin)):
        if b_bin[i] == str(1):
            print(i)
            circuit.x(i)

    for i in range(len(a_bin)):
        if a_bin[i] == str(1):
            circuit.x(len(b_bin)+i)

    return circuit


def quantum_multiplication(a, b, digits):
    a_bin = f'{a:0{digits}b}'
    b_bin = f'{b:0{digits}b}'
    circuit = preparation(a_bin, b_bin)
    print(circuit)
    circuit.barrier()

    # # QFT on the ancilla
    circuit.append(QFT(1).to_gate(), qargs = [2*len(b_bin)])

    circuit.measure_all()
    return circuit


# Run the simulation
a = 1
b = 2
digits = 3

sol = quantum_multiplication(a, b, digits)
print(sol)

# simulator = AerSimulator()
# qct = transpile(sol, simulator)

# result = Aer.get_backend('statevector_simulator').run(qct, shots=1).result()
# counts = result.get_counts()
# print(counts)

