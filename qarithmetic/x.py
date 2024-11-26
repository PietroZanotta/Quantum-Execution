from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, transpile
from qiskit_aer import AerSimulator, Aer
from QArithmetic import bitwise_and

# Registers and circuit.
a = QuantumRegister(4)
b = QuantumRegister(4)
c = QuantumRegister(4)
ca = ClassicalRegister(4)
cb = ClassicalRegister(4)
cc = ClassicalRegister(4)
qc = QuantumCircuit(a, b, c, ca, cb, cc)

# Inputs
qc.x(a[1]) # a =1010
qc.x(a[3])
qc.x(b[0]) # b = 1011
qc.x(b[1])
qc.x(b[3])

# Take the bitwise AND.
bitwise_and(qc, a, b, c, 4)

# Measure.
qc.measure(a, ca)
qc.measure(b, cb)
qc.measure(c, cc)

print(qc.depth())
print(qc.size())