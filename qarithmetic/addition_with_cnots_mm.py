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

def remove_small_elements(expr, threshold=1e-6):
    return expr.xreplace({x: 0 if abs(x) < threshold else x for x in expr.atoms() if x.is_number})

a = QuantumRegister(3)
b = QuantumRegister(3)
qc = QuantumCircuit(a, b)

qc.barrier()

# cnots
for i in range(0, 3):
    qc.cx(a[i], b[i])

# Add the numbers, so |a>|b> to |a>|a+b>.
print(qc)
add(qc, a, b, 2)

matrix = Operator(qc).data
binary_variables = [f'{i:06b}'[::-1] for i in range(2**(6))] 
# binary_variables = [f'x{i}' for i in range(2**(6))] 
variables = symbols(binary_variables)

vector = Matrix(variables)
M = Matrix(matrix)  
result = M * vector

init_printing()
result_simplified = result.applyfunc(lambda x: remove_small_elements(x))

init_printing()
pretty_print(result_simplified)
pretty_print(vector)
