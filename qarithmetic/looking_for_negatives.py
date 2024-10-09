from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, transpile
from qiskit_aer import AerSimulator, Aer
from QArithmetic import add, mult, div, sub
from math import pi

from qiskit.quantum_info import Operator
import numpy as np
np.set_printoptions(precision=3, suppress=True, threshold=np.inf)
from sympy import Matrix, pretty_print
from qft import qft, iqft, cqft, ciqft, ccu1


def find_negatives(matrix):
    matrix = np.where(np.abs(matrix) < 1e-5, 0, matrix)
    negatives_indices = np.argwhere(matrix < 0)
    
    if negatives_indices.size == 0:
        print("No negative numbers found in the matrix.")
    else:
        for idx in negatives_indices:
            print(f"Negative number {matrix[tuple(idx)]} found at position {tuple(idx)}")

# Add the numbers, so |a>|b> to |a>|a+b>.
# def add(circ, a, b, n):
#     n += 1
#     qft(circ, b, n)
#     matrix = Operator(circ).data
#     find_negatives(matrix)

#     print("\n\n")
#     print("addition part")
#     for i in range(n, 0, -1):
#         for j in range(i, 0, -1):
#             if len(a) - 1 >= j - 1:
#                 circ.cp(2*pi/2**(i-j+1), a[j-1], b[i-1]) 
#                 print("\n\n")
#                 print("cp")
#                 matrix = Operator(circ).data
#                 find_negatives(matrix)
     
    
#     iqft(circ, b, n)
#     print("\n\n")
#     print("addition part")
#     matrix = Operator(circ).data
#     find_negatives(matrix)


#############################################################
print("\n\nADD:")
num = 3

a = QuantumRegister(num)
b = QuantumRegister(num)
cb = ClassicalRegister(num)
qc = QuantumCircuit(a, b, cb)  

add(qc, a, b, num-1)

matrix = Operator(qc).data
find_negatives(matrix)

#############################################################
print("\n\nSUB:")
num = 3

a = QuantumRegister(num)
b = QuantumRegister(num)
cb = ClassicalRegister(num)
qc = QuantumCircuit(a, b, cb)  

sub(qc, a, b, num-1)

matrix = Operator(qc).data
find_negatives(matrix)

#############################################################
print("\n\nMULT:")
num = 2

a = QuantumRegister(num)
b = QuantumRegister(num)
m = QuantumRegister(2*num)
cm = ClassicalRegister(2*num)
qc = QuantumCircuit(a, b, m, cm)

mult(qc, a, b, m, num)

matrix = Operator(qc).data
find_negatives(matrix)

#############################################################
print("\n\nDIV:")
num = 2

a = QuantumRegister(2*num)
b = QuantumRegister(2*num)
c = QuantumRegister(num)
ca = ClassicalRegister(2*num)
cb = ClassicalRegister(2*num)
cc = ClassicalRegister(num)
qc = QuantumCircuit(a,b,c,ca, cc)

div(qc, b, a, c, 2)
matrix = Operator(qc).data
find_negatives(matrix)

#############################################################
print("\n\nINV ADD:")
num = 3

a = QuantumRegister(num)
b = QuantumRegister(num)
circ_fin = QuantumCircuit(2*num)
cb = ClassicalRegister(num)
qc = QuantumCircuit(a, b)  

add(qc, a, b, num-1)
circ_fin.append(qc, range(0, 2*num))

matrix = Operator(circ_fin).data
find_negatives(matrix)

#############################################################
print("\n\nINV SUB:")
num = 3

a = QuantumRegister(num)
b = QuantumRegister(num)
circ_fin = QuantumCircuit(2*num)
cb = ClassicalRegister(num)
qc = QuantumCircuit(a, b)  

sub(qc, a, b, num-1)
circ_fin.append(qc, range(0, 2*num))

matrix = Operator(circ_fin).data
find_negatives(matrix)

#############################################################
print("\n\nINV MULT:")
num = 2

a = QuantumRegister(num)
b = QuantumRegister(num)
m = QuantumRegister(2*num)
circ_fin = QuantumCircuit(4*num)
cm = ClassicalRegister(2*num)
qc = QuantumCircuit(a, b, m)

mult(qc, a, b, m, num)

circ_fin.append(qc, range(0, 4*num))

matrix = Operator(circ_fin).data
find_negatives(matrix)

#############################################################
print("\n\nINV DIV:")
num = 2

a = QuantumRegister(2*num)
b = QuantumRegister(2*num)
c = QuantumRegister(num)
circ_fin = QuantumCircuit(5*num)
ca = ClassicalRegister(2*num)
cb = ClassicalRegister(2*num)
qc = QuantumCircuit(a,b,c)

div(qc, b, a, c, 2)

circ_fin.append(qc, range(0, 5*num))

matrix = Operator(qc).data
find_negatives(matrix)