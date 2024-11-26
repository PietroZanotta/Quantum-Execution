from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, transpile
from qiskit_aer import AerSimulator, Aer
from QArithmetic import add, qft


n = 4

a = QuantumRegister(n)
b = QuantumRegister(n)
cb = ClassicalRegister(n)
qc = QuantumCircuit(a, b, cb)

add(qc, a, b, n-1)

print(qc)
print(qc.size())

print(int(2*(0-n*(n+1)/2 + n**2 + n) + n**2 +n - n*(n+1)/2))

# print(qc.depth())