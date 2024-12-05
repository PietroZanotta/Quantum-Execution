"""
{
    int x = input;

    // 1
    if (n<3) {
    return n;
    }
    n--;

    // 2
    if (n<3) {
    return n;
    }
    n--;

    // 3
    if (n<3) {
    return n;
    }
    n--;

    // 4
    if (n<3) {
    return n;
    }
    n--;

    // 5
    if (n<3) {
    return n;
    }
    n--;

}

"""

from math import sqrt
import itertools
import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, transpile, ClassicalRegister
import matplotlib.pyplot as plt
from qiskit_aer import AerSimulator, Aer
from QArithmetic import add, div, cadd, sub

x = QuantumRegister(4, name = "x")
ancilla = QuantumRegister(5, name = "anc")
one_or_four = QuantumRegister(4, name = "1 or 5")

cx = ClassicalRegister(4)
cx2 = ClassicalRegister(4)
cq = ClassicalRegister(4)
canc = ClassicalRegister(5)
qc = QuantumCircuit(x, one_or_four, ancilla, cx)#, cx2, canc)

qc.h(x[0:3]) # 0000 0abc

for i in range(0, 5):
    qc.x(one_or_four[2]) # 0100
    qc_ = QuantumCircuit(x, one_or_four)
    add(qc_, one_or_four, x, 3)

    qc.append(qc_, range(0, 8))
    qc.cx(x[3], ancilla[i])
    qc.append(qc_.inverse(), list(x) + list(one_or_four))

    qc.x(one_or_four[2])
    qc.cx(ancilla[i], one_or_four[0]) # 0001

    sub(qc, x, one_or_four, 4)
    
    for i in range(0, 4):
        qc.swap(x[i], one_or_four[i])

    qc.reset(one_or_four)


# measure and run
qc.measure(x, cx)
# qc.measure(one_or_four, cx2)
# qc.measure(ancilla, canc)

qct = transpile(qc, AerSimulator())

result = Aer.get_backend('statevector_simulator').run(qct, shots=50).result()
counts = result.get_counts()

print(qc)
# print(counts)
integer_dict = {int(key, 2): value for key, value in counts.items()}

print(integer_dict)
