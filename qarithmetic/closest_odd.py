from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, transpile
from qiskit_aer import AerSimulator, Aer
from QArithmetic import add, mult, div, sub, cadd
from math import pi

a = QuantumRegister(6)
b = QuantumRegister(6)
c = QuantumRegister(3)
is_3 = QuantumRegister(1)
is_odd = QuantumRegister(1)
is_odd_c = ClassicalRegister(1)
ca = ClassicalRegister(6)
cb = ClassicalRegister(6)
cc = ClassicalRegister(3)
c_res = ClassicalRegister(3)
qc = QuantumCircuit(a,b,c,is_3, is_odd, c_res)#, ca,cb,cc, is_odd_c)


# init

# a = 0-7 # 3/4 = 000 100 / 000 011
qc.h(a[0])
qc.h(a[1])
qc.h(a[2])

# qc.x(a[0])
# qc.cx(a[0], a[2])
# qc.x(a[0])

qc.cx(a[0], a[1])

# b = 2 # 010 000
qc.x(b[4])

# create the is_odd subroutine (in this simple case only look if the number is even or odd)
is_odd_qc = QuantumCircuit(a, b, c, is_odd, name="/ 2")

div(is_odd_qc, a, b, c, 3)

qc.append(is_odd_qc, list(range(0, 15)) + [qc.num_qubits-1])

# cnot
qc.cx(a[3], is_odd)

qc.append(is_odd_qc.inverse(), list(range(0, 15)) + [qc.num_qubits-1])

# +1 on even numbers
qc.x(is_odd)

# encode 1 in c
qc.x(c[0])

cadd(qc, is_odd, c, range(0, 3), 2)

qc.x(c[0])

qc.measure(range(0,3), (c_res))


# Simulate the circuit.
simulator = AerSimulator()
qct = transpile(qc, simulator)
# print(qct)

result = Aer.get_backend('statevector_simulator').run(qct, shots=100).result()
counts = result.get_counts()
print(counts)
# print(qc)
