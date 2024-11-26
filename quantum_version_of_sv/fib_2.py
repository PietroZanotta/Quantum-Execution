# unroled fibonacci (working with inputs <= 2)
"""
    x=input
    if x - 1 < 0: 
        result = 0
    if x == 1: 
        result = 1
    else:   
        if x-2 == 0:
            x2 = 1
        if x-2 < 0:
            x2 = 0
        
        if x-3 == 0:
            x1 = 1 # never happens
        if x-3 < 0:
            x1 = 0

    result = x1 + x2
"""


from math import sqrt
import itertools
import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, transpile, ClassicalRegister
import matplotlib.pyplot as plt
from qiskit_aer import AerSimulator, Aer
from QArithmetic import sub, add

x = QuantumRegister(4, name = "x")
x1 = QuantumRegister(4, name = "x-3")
x2 = QuantumRegister(4, name = "x-2")

subtractor_main = QuantumRegister(4, name = "subtractor-main")
ancilla = QuantumRegister(6, name = "ancilla")

cx = ClassicalRegister(4)
cx1 = ClassicalRegister(4)
cx2 = ClassicalRegister(4)
canc = ClassicalRegister(6)
qc = QuantumCircuit(x, x1, x2, subtractor_main, ancilla, cx2)

# init superposition
qc.initialize([1/sqrt(3), 1/sqrt(3), 1/sqrt(3), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], x)

qc.barrier()

# if x - 1 < 0: 
#   result = 0
# if x - 1 == 0: 
#   return = 1
qc.x(subtractor_main[0])
sub(qc, subtractor_main, x, 4)
qc.cx(x[3], ancilla[0])

qc.x(x)
qc.mcx(x, ancilla[1])
qc.x(x)

add(qc, subtractor_main, x, 3)

qc.cx(ancilla[1], x1[0]) # result = 1

# else:   
qc.x(ancilla[0:2])

#     if x-2 == 0:
#        x2 = 1
#   if x-2 < 0:
#         x2 = 0
x_sub = QuantumRegister(4, name = "x")
x1_sub = QuantumRegister(4, name = "x1_sub")
x2_sub = QuantumRegister(4, name = "x2_sub")
subtractor = QuantumRegister(4, name = "subtractor")
ancilla_sub = QuantumRegister(4, name = "ancilla")
subcircuit = QuantumCircuit(x_sub, x1_sub, x2_sub, subtractor, ancilla_sub, name = "x-2")

subcircuit.x(subtractor[0]) # 0010
subcircuit.x(subtractor[1])

sub(subcircuit, subtractor, x_sub, 4)

subcircuit.cx(x_sub[3], ancilla_sub[0]) # never happens

subcircuit.x(x_sub)
subcircuit.mcx(x_sub, ancilla_sub[1])
subcircuit.x(x_sub)

add(subcircuit, subtractor, x_sub, 3)

subcircuit.cx(ancilla_sub[1], x2_sub[0]) # x2 = 1

#   if x-3 == 0:
#         x1 = 1 # never happens
#   if x-3 < 0:
#         x1 = 0
subcircuit.x(subtractor[0]) # 0011

sub(subcircuit, subtractor, x_sub, 4)

subcircuit.cx(x_sub[3], ancilla_sub[2]) # this always happens

subcircuit.x(x_sub)
subcircuit.mcx([x_sub[0], x_sub[1], x_sub[2], x_sub[3]], ancilla_sub[3]) # never happens
subcircuit.x(x_sub)

add(subcircuit, subtractor, x_sub, 3)

subcircuit.cx(ancilla_sub[3], x1_sub[0]) # x1 = 1. should be 0 in every case

# append
subcircuit = subcircuit.to_gate()
controlled_sub_gate = subcircuit.control(2)  
qc.append(controlled_sub_gate, [ancilla[0], ancilla[1], x[0], x[1], x[2], x[3], x1[0], x1[1], x1[2], x1[3], x2[0], x2[1], x2[2], x2[3], subtractor_main[0], subtractor_main[1], subtractor_main[2], subtractor_main[3], ancilla[2], ancilla[3], ancilla[4], ancilla[5]])  

add(qc, x1, x2, 2)

# qc.measure(x, cx)
qc.measure(x2, cx2)
# qc.measure(x1, cx1)
# qc.measure(ancilla, canc)

# Run the simulation
qct = transpile(qc, AerSimulator())

result = Aer.get_backend('statevector_simulator').run(qct, shots=10).result()
counts = result.get_counts()

print(qc)
print(counts)
