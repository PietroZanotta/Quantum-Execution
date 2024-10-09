from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit.quantum_info import Operator
from qiskit_aer import Aer, AerSimulator
from QArithmetic import add
from sympy import Matrix, I, nsimplify, Rational
import numpy as np; np.set_printoptions(threshold=np.inf, linewidth=np.inf)


# addition
a_circ = QuantumRegister(2, name="a")
b_circ = QuantumRegister(2, name="b")
ancilla_circ = QuantumRegister(1, name="ancilla")
cr = ClassicalRegister(2)
qc = QuantumCircuit(a_circ, b_circ)
qc_total = QuantumCircuit(a_circ, b_circ, ancilla_circ)

add(qc, a_circ, b_circ, 1)

# inverse addition
qc_inv = qc.inverse()



qc_total.append(qc, range(0, 2*2))
qc_total.cx(2, 4)
qc_total.append(qc_inv, range(0, 2*2))


print(transpile(qc_total, AerSimulator()))

# Get the matrix representation
matrix = Operator(qc_total).data
print(matrix)
# sympy_matrix = Matrix(matrix)

# print(matrix)
# simplified_matrix = simplify_complex_matrix(sympy_matrix)
# print(simplified_matrix)


# simulator = AerSimulator()
# qct = transpile(qc, simulator)
# print(qct)

# result = Aer.get_backend('statevector_simulator').run(qct, shots=1024).result()
# counts = result.get_counts()
# print(counts)

# print(simplified_matrix.shape)
