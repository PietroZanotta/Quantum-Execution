from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, transpile
from qiskit_aer import AerSimulator, Aer
from QArithmetic import mult, cqft

n=4

# Registers and circuit.
a = QuantumRegister(n)
b = QuantumRegister(n)
m = QuantumRegister(2*n)
cm = ClassicalRegister(2*n)
qc = QuantumCircuit(a, b, m, cm)

mult(qc, a, b, m, n-1)

print(qc)
print("true size: " + str(qc.size()))


def qft_size(a):
    return (a*n)**2 + a*n - a*n*(a*n+1)/2

def cqft_size(a, n):
    return a*(n)**2 + n - a*n*(n+1)/2

print(int((2*(n-1))*(cqft_size(5, n))+ (n-1)*(qft_size(1))))


# qc = QuantumCircuit(a, cm)
# cqft(qc, 0, a[1::], n-1)
# print("true size: " + str(qc.size()))
# print(int((cqft_size(5, n-1))))

# print(qc)

print(qc.depth())