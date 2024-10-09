from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, transpile
from qiskit_aer import AerSimulator, Aer
from QArithmetic import add

# Registers and circuit.
a = QuantumRegister(4)
b = QuantumRegister(5)
cb = ClassicalRegister(5)
qc = QuantumCircuit(a, b, cb)

# Numbers to add.
qc.x(a[1]) # a = 01110
qc.x(a[2])
qc.x(a[3])
qc.h(b[0]) # b = 01011 / 01010
qc.x(b[1])
qc.x(b[3])

# qc.x(a[1]) # 1010
# qc.x(a[3]) # 00001
# qc.x(b[0])


qc.barrier()

# Add the numbers, so |a>|b> to |a>|a+b>.
add(qc, a, b, 4)

# Measure the results.
qc.barrier()
qc.measure(b, cb)

# Simulate the circuit.
simulator = AerSimulator()
qct = transpile(qc, simulator)
print(qct)

result = Aer.get_backend('statevector_simulator').run(qct, shots=1024).result()
counts = result.get_counts()
print(counts)
