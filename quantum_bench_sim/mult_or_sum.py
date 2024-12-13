from math import sqrt
import itertools
import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, transpile, ClassicalRegister
import matplotlib.pyplot as plt
from qiskit_aer import AerSimulator, Aer
from QArithmetic import add, div, cadd, sub, mult


a = QuantumRegister(3)
b = QuantumRegister(3)
c = QuantumRegister(3)
d = QuantumRegister(3)
anc = QuantumRegister(2)
mult_reg = QuantumRegister(6)

ca = ClassicalRegister(3)
cb = ClassicalRegister(3)
cc = ClassicalRegister(3)
cd = ClassicalRegister(3)
canc = ClassicalRegister(3)
cmult_reg = ClassicalRegister(6)

qc = QuantumCircuit(anc, a, b, c, d, mult_reg, ca)

#init variables
qc.h(a[0]) # 010 or 001
qc.x(a[1])
qc.cx(a[0], a[1])

qc.h(b[2]) # 011 or 100
qc.x(b[1])
qc.x(b[0])
qc.cx(b[2], b[1])
qc.cx(b[2], b[0])

qc.h(c[0]) # 010 or 001
qc.x(c[1])
qc.cx(c[0], c[1])

qc.h(d[0]) # 010 or 001
qc.x(d[1])

# h, cx, x
qc.h(anc[0])
qc.cx(anc[0], anc[1])
qc.x(anc[1])

# cadd
cadd(qc, anc[0], a, b, 2)

#mult_reg
qc_ = QuantumCircuit(c, d, mult_reg)

# qc_.h(c[0]) # 010 or 001
# qc_.x(c[1])
# qc_.cx(c[0], c[1])

# qc_.h(d[0]) # 010 or 001
# qc_.x(d[1])

mult(qc_, d, c, mult_reg, 3)


qc_ = qc_.to_gate().control(1)
qc.append(qc_, [1] + list(range(8, qc.num_qubits)))

#cswap b or a+b to d or c*d
for i in range(3):
    qc.cswap(anc[1], mult_reg[i], b[i])


qc.measure(b, ca)

qct = transpile(qc, AerSimulator())

result = Aer.get_backend('statevector_simulator').run(qct, shots=200).result()
counts = result.get_counts()

print(qc)
print(counts)
# print(counts)
integer_dict = {int(key, 2): value for key, value in counts.items()}
print(integer_dict)