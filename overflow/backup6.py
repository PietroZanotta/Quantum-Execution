"""
if x*2 >= 10:
    return x+1
else:
    return x
"""

from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, transpile
from qiskit_aer import AerSimulator, Aer
from QArithmetic import mult, add, cadd
from fpqs6 import fpqs_circ
import matplotlib.pyplot as plt

# Registers and circuit.
a = QuantumRegister(4)
x = QuantumRegister(4)
m = QuantumRegister(8)
anc = QuantumRegister(2)
c_anc = ClassicalRegister(2)
cm = ClassicalRegister(4)
qc = QuantumCircuit(a, x, m, anc, cm)
qc_new = QuantumCircuit(a, x, m, anc, cm)

# Numbers to multiply.
qc_new.x(a[1]) # a = 0010 / 0011
qc_new.h(a[0])

qc_new.h(x[0]) # x = from 0000 to 0111
qc_new.h(x[1])
qc_new.h(x[2])

# Multiply the numbers, so |a>|x>|m=0> to |a>|x>|a*x>.
mult(qc, a, x, m, 3)

# Encode |9> in a register
qc_new.x(a[1])
qc_new.h(a[0])
qc_new.x(a[0]) # 1001 
# qc_new.x(a[3])



# m+9
add(qc, a, m, 4)
qc_inv = qc.inverse()
qc_new.append(qc, range(0, len(qc.qubits)), range(0, len(qc.clbits)))

# # first qubit indicates if 2/3*x >= 7
# qc_new.barrier()
# qc_new.cx(m[4], anc[0])

# revert the *2/3 and +9
# qc_new.append(qc_inv, range(0, len(qc.qubits)), range(0, len(qc.clbits)))

# # encode |1> in a register
# qc_new.x(a[1])
# qc_new.x(a[2])
# qc_new.x(a[0]) # 0001 

# # controlled x+1
# cadd(qc_new, anc[0], a, x, 3)

# # x gate to the first ancilla to act on the other qubits
# qc_new.x(anc[0])

# # encode |5> in a register
# qc_new.x(a[0])
# qc_new.x(a[0])
# qc_new.x(a[2])


# # controlled x+7
# cadd(qc_new, anc[0], a, x, 3)

# # fpqs
# def oracle(qc, num_qubits):
#     # oracle to observe if an overflow happened
#     qc.cx(7, 17)

# A = qc_new

# # Perform fixed-point quantum search
# fpqs_qc = fpqs_circ(oracle, .5, 4, A, 3)
# qc_new.append(fpqs_qc, range(0, 18), range(0,4))

# # Measure the result
# qc_new.barrier()
qc_new.measure(x, (cm))
# qc_new.measure(anc, c_anc)

# Simulate the circuit.
simulator = AerSimulator()
qct = transpile(qc_new, simulator)
# print(qct)

result = Aer.get_backend('statevector_simulator').run(qct, shots=100).result()
counts = result.get_counts()
# print(counts)
decimal_dict = {int(key, 2): value for key, value in counts.items()}

sorted_dict = dict(sorted(decimal_dict.items()))

print(sorted_dict)




plt.figure(figsize=(10, 5))
plt.bar(counts.keys(), counts.values())
plt.xlabel('States')
plt.ylabel('Frequency')
plt.xticks(rotation=90)
plt.tight_layout()
# plt.show()

#  ░  ░  