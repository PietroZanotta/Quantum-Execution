from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, transpile
from qiskit_aer import AerSimulator, Aer
from QArithmetic import div

# Registers and circuit.
a = QuantumRegister(4)
b = QuantumRegister(4)
c = QuantumRegister(2)
ca = ClassicalRegister(4)
cb = ClassicalRegister(4)
cc = ClassicalRegister(2)
qc = QuantumCircuit(a,b,c,ca, cc)

# Inputs.
qc.x(a[1]) # a = 0010 / 0011
qc.h(a[0])

qc.x(b[3]) # b = 1000

# Divide b by a.
div(qc, b, a, c, 2)


# Measure.
qc.barrier()
qc.measure(a, (ca))
# qc.measure(b, cb)

qc.measure(c, (cc))

# Simulate the circuit.
simulator = AerSimulator()
qct = transpile(qc, simulator)
print(qct)

result = Aer.get_backend('statevector_simulator').run(qct, shots=1024).result()
counts = result.get_counts()
print(counts)
