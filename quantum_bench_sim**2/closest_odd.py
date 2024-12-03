"""
num=input

if(!num % 2 == 0){
    return num;
} else {
    return num + 1;
}

"""


from math import sqrt
import itertools
import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, transpile, ClassicalRegister
import matplotlib.pyplot as plt
from qiskit_aer import AerSimulator, Aer
from QArithmetic import add, div, cadd

x = QuantumRegister(8, name = "x")
q = QuantumRegister(4, name = "q")
ancilla = QuantumRegister(1, name = "anc")
one_or_two = QuantumRegister(8, name = "1")

cx = ClassicalRegister(8)
cx2 = ClassicalRegister(8)
cq = ClassicalRegister(4)
canc = ClassicalRegister(1)
qc = QuantumCircuit(x, q, ancilla, one_or_two, cx)#, cx2, cq, canc)

# init superposition
qc.h(x[0:3]) # 0000 0abc
# qc.x(x[3])

qc.barrier()
qc.x(one_or_two[5]) # 0010 0000

# if(!num % 2 == 0){
x_ = QuantumRegister(8, name = "x")
q_ = QuantumRegister(4, name = "q")
ancilla_ = QuantumRegister(1, name = "anc")
one_or_two_ = QuantumRegister(8, name = "1")

qc_ = QuantumCircuit(x, q, ancilla, one_or_two)

div(qc_, x_, one_or_two_, q_, 4)

qc.append(qc_, range(0, qc.num_qubits))

qc.cx(x[4], ancilla[0])

qc.append(qc_.inverse(), range(0, qc.num_qubits))
qc.x(ancilla)

# else {
#   return num + 1;
# }
qc.x(one_or_two[4])
qc.x(one_or_two[5])

cadd(qc, ancilla[0], one_or_two[4:8], x[0:4], 3)

# measure and run
qc.measure(x, cx)
# qc.measure(one_or_two, cx2)
# qc.measure(q, cq)
# qc.measure(ancilla, canc)

qct = transpile(qc, AerSimulator())

result = Aer.get_backend('statevector_simulator').run(qct, shots=20).result()
counts = result.get_counts()

print(qc)
# print(counts)
integer_dict = {int(key, 2): value for key, value in counts.items()}

print(integer_dict)
