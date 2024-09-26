from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, transpile
from qiskit_aer import AerSimulator, Aer
from QArithmetic import sub

# Registers and circuit.
a = QuantumRegister(5)
b = QuantumRegister(5)
# ca = ClassicalRegister(5)
cb = ClassicalRegister(5)
qc = QuantumCircuit(a, b, cb)

# Numbers to subtract.
qc.x(a[1]) # a = 01110
qc.x(a[2])
qc.x(a[3])
qc.h(b[0]) # b = 01010 / 01011
qc.x(b[1])
qc.x(b[3])

# Add the numbers, so |a>|b> to |a>|a-b>.
sub(qc, a, b, 5)

# Measure the results.
# qc.measure(a, ca)
qc.measure(b, cb)

# Simulate the circuit.
simulator = AerSimulator()
qct = transpile(qc, simulator)
print(qct)

result = Aer.get_backend('statevector_simulator').run(qct, shots=1024).result()
counts = result.get_counts()
print(counts)