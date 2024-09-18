import math
import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, transpile
from qiskit.circuit.library import QFT, SGate, SdgGate, TGate, TdgGate
import matplotlib.pyplot as plt
from qiskit_aer import AerSimulator, Aer


def preparation(a_bin, b_bin):
    # Encoding a and b into quantum states
    num_qubits = len(a_bin) + len(b_bin)    
    circuit = QuantumCircuit(num_qubits)


    for i in range(len(b_bin)):
        if b_bin[i] == str(1):
            circuit.x(i)

    for i in range(len(a_bin)):
        if a_bin[i] == str(1):
            circuit.x(len(b_bin)+i)

    return circuit


def qft(circuit, qubits_range):
    # compute QFT
    for tar in qubits_range:
        circuit.h(tar)
        for contr in range(tar+1, np.max(qubits_range)+1):
            circuit.cp(2*math.pi/(2**(contr - tar + 1)), contr, tar)
        circuit.barrier()


def iqft(circuit, qubits_range):
    #compute IQFT
    for tar in reversed(qubits_range):
        circuit.h(tar)
        for contr in reversed(range(np.min(qubits_range), tar)):
            print(str(contr) + " su " + str(tar))
            circuit.cp(-2*math.pi/(2**(tar - contr + 1)), contr, tar)
        circuit.barrier()


def quantum_addition(a, b, digits):
    # adds two numbers
    a_bin = f'{a:0{digits}b}'
    b_bin = f'{b:0{digits}b}'
    print(a_bin)
    print(b_bin)
    circuit = preparation(a_bin, b_bin)
    circuit.barrier()

    # QFT on the a register and the ancilla
    qft(circuit, range(len(b_bin), 2*len(b_bin)))

    circuit.barrier()

    qubits_range = range(int(len(circuit.qubits)/2), len(circuit.qubits))

    CSGate = SGate().control(1)
    CTGate = TGate().control(1)

    for tar in range(len(b_bin), len(b_bin)*2):
        for contr in range(tar - len(b_bin), len(b_bin)):
            circuit.cp(2*math.pi / (2**(len(b_bin) - (tar - contr) + 1)), contr, tar)
        circuit.barrier()

    # IQFT on the a register
    iqft(circuit, range(len(b_bin), 2*len(b_bin)))

    circuit.measure_all()
    return circuit


# Run the simulation
b = 3
a = 2
digits = 4

sol = quantum_addition(a, b, digits)
print(sol)

simulator = AerSimulator()
qct = transpile(sol, simulator)

result = Aer.get_backend('statevector_simulator').run(qct, shots=1024).result()
counts = result.get_counts()
print(counts)
