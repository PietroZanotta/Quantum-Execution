from sympy import symbols, Matrix
from sympy import init_printing, pretty_print
import re
import numpy as np

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit.quantum_info import Operator
from qiskit_aer import Aer, AerSimulator
from QArithmetic import add
from sympy import Matrix, I, nsimplify, Rational
import numpy as np; np.set_printoptions(threshold=np.inf, linewidth=np.inf)


a = QuantumRegister(3)
b = QuantumRegister(3)
ca = ClassicalRegister(3)
cb = ClassicalRegister(3)
qc = QuantumCircuit(a, b, cb, ca)


qc.h(a[0]) # 001


qc.barrier()

# cnots
for i in range(0, 3):
    qc.cx(a[i], b[i])

# Add the numbers, so |a>|b> to |a>|a+b>.
print(qc)
add(qc, a, b, 2)

qc.barrier()
qc.measure(a, ca)
qc.measure(b, cb)

# Simulate the circuit.
simulator = AerSimulator()
qct = transpile(qc, simulator)
print(qct)

result = Aer.get_backend('statevector_simulator').run(qct, shots=1024).result()
counts = result.get_counts()
print(counts)