from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, transpile
from qiskit_aer import AerSimulator, Aer
from QArithmetic import mult

# Registers and circuit.
a = QuantumRegister(2)
b = QuantumRegister(2)
m = QuantumRegister(4)
cm = ClassicalRegister(4)
qc = QuantumCircuit(a, b, m, cm)

# Numbers to multiply.
qc.x(a[1]) # a = 10
qc.h(b[0]) # b = 10 / 11
qc.x(b[1])

# Multiply the numbers, so |a>|b>|m=0> to |a>|b>|a*b>.
mult(qc, a, b, m, 2)

# Measure the result.
qc.measure(m, cm)

# Simulate the circuit.
simulator = AerSimulator()
qct = transpile(qc, simulator)
print(qct)

result = Aer.get_backend('statevector_simulator').run(qct, shots=1024).result()
counts = result.get_counts()
print(counts)