from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, transpile
from qiskit_aer import AerSimulator, Aer
from QArithmetic import power

# Registers and circuit.
a = QuantumRegister(2)
b = QuantumRegister(2)
m = QuantumRegister(4)
cm = ClassicalRegister(4)
qc = QuantumCircuit(a, b, m, cm)

# Inputs.
qc.x(a[1]) # a = 10
qc.x(b[1]) # b = 10 / 11
qc.h(b[0])

# Raise a to the b power.
power(qc, a, b, m)

# Measure the result.
qc.measure(m, cm)

# Simulate the circuit.
simulator = AerSimulator()
qct = transpile(qc, simulator)
print(qct)

result = Aer.get_backend('statevector_simulator').run(qct, shots=10).result()
counts = result.get_counts()
print(counts)