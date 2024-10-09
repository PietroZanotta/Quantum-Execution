from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, transpile
from qiskit_aer import AerSimulator, Aer
from QArithmetic import add
from numpy.random import uniform, choice


# Registers and circuit.
x = QuantumRegister(4, name="x")
y = QuantumRegister(4, name="y")
a_b = ClassicalRegister(8, name="ab")

z = QuantumRegister(4, name="z")
q = QuantumRegister(4, name="q")
c_d = ClassicalRegister(8, name="cd")
qc = QuantumCircuit(x,y,z,q,a_b,c_d)
init = QuantumCircuit(x,y,z,q, name="init")

# random H to produce the numbers to be added
# for i in range(0, int(uniform(0, 8))):
#     tarx = int(uniform(0,4))
#     init.h(x[tarx])

# for i in range(0, int(uniform(0, 8))):
#     tary = int(uniform(0,4))
#     init.h(y[tary])

# for i in range(0, int(uniform(0, 8))):
#     tarz = int(uniform(0,4))
#     init.h(z[tarz])

# for i in range(0, int(uniform(0, 8))):
#     tarq = int(uniform(0,4))
#     init.h(q[tarq])

init.x(x[0]) # 0001

init.x(y[0]) # 0101
init.x(y[2])

# init.x(z[2]) # 1100
# init.x(z[3])

init.x(q[2]) # 0100

# exp result:
# a_b = 01110001
# c_d = 10100110

qc.append(init, range(0, qc.num_qubits))

# x+y
qc.barrier()
add1 = QuantumCircuit(x,y,z,q, name="+1")
add1_inv = add1.inverse()
add(add1, x, y, 3)
qc.append(add1, range(0, int(qc.num_qubits)))

# cnots
qc.barrier()
for i in range(0, int(qc.num_qubits/4)):
    qc.cx(y[i], z[i]) 

# z + q
qc.barrier()
add2 = QuantumCircuit(x,y,z,q, name="+2")
add2_inv = add2.inverse()
add(add2, x, y, 3)
qc.append(add2, range(0, int(qc.num_qubits)))

# x + y
qc.barrier()
add3 = QuantumCircuit(x,y,z,q, name="+3")
add3_inv = add3.inverse()
add(add3, z, q, 3)
qc.append(add3, range(0, int(qc.num_qubits)))

# reverse
# qc.append(add3_inv, range(0, int(qc.num_qubits)))
# qc.append(add2_inv, range(0, int(qc.num_qubits)))
# qc.append(add1_inv, range(0, int(qc.num_qubits)))
# qc.append(init.inverse(), range(0, int(qc.num_qubits)))

qc.barrier()

qc.measure(range(0, 8), a_b)
qc.measure(range(8, 16), c_d) # 10100110

print(qc)
# print(init)


# Simulate the circuit.
simulator = AerSimulator()
qct = transpile(qc, simulator)
# print(qct)

result = Aer.get_backend('statevector_simulator').run(qct, shots=1024).result()
counts = result.get_counts()
print(counts)
