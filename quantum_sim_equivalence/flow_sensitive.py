"""
if x >= 4:          (4,5,6,7)
    if x >= 5:
        x+=1        (4,6,7,8)
    else:           
        x+=5        (9,6,7,8)       
        
else:               (0,1,2,3)
    if x >= 2:       
        x+=5        (0,1,7,8)

return x        (0,1,6,7,8,9)
"""

from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, transpile
from qiskit_aer import AerSimulator, Aer
import matplotlib.pyplot as plt
from QArithmetic import add, cadd, sub


# Registers and circuit.
b = QuantumRegister(4)
x = QuantumRegister(4)
anc = QuantumRegister(4)
cb = ClassicalRegister(4)
cx = ClassicalRegister(4)
canc = ClassicalRegister(4)
qc = QuantumCircuit(b, x, name="+4")# cc, cx, cb, cm, canc)
qc_new = QuantumCircuit(b, x, anc, cx)#, cb, cm, canc, cc)#cc, cx, cb, cm, canc)


# Registers and circuit.
b = QuantumRegister(4)
x = QuantumRegister(4)
anc = QuantumRegister(4)
cb = ClassicalRegister(4)
cx = ClassicalRegister(4)
canc = ClassicalRegister(4)
qc = QuantumCircuit(b, x, name="+4")# cc, cx, cb, cm, canc)
qc_new = QuantumCircuit(b, x, anc, cx)#, cb, cm, canc, cc)#cc, cx, cb, cm, canc)

# Init
qc_new.h(x[0]) # x = from 0000 to 0111 
qc_new.h(x[1])
qc_new.h(x[2])


qc_new.x(b[2]) # b = 0100

# x+4, in anc[0] goes the overflow
add(qc, b, x, 3)

qc_inv = qc.inverse()
qc_new.append(qc, range(0, len(qc.qubits)), range(0, len(qc.clbits)))

# cnot
qc_new.cx(x[3], anc[0])

# revert the +4
qc_new.append(qc_inv, range(0, len(qc.qubits)), range(0, len(qc.clbits)))

# controlled +3 based on a1
qc_new.x(b[0])
qc_new.x(b[1])
qc_new.x(b[2])

qc = QuantumCircuit(b, x, anc, name="c+3")
cadd(qc, anc[0], b, x, 3)

qc_new.append(qc, range(0, len(qc.qubits)), range(0, len(qc.clbits)))

qc_inv = qc.inverse()

qc_new.cx(x[3], anc[1])

qc_new.append(qc_inv, range(0, len(qc.qubits)), range(0, len(qc.clbits)))

# nested if +1
qc_new.x(b[1])

qc = QuantumCircuit(b, x, name="cc+1")
add(qc, b, x, 3)

qc_ctrl = qc.to_gate().control(2)

qc_new.append(qc_ctrl, list(range(len(qc.qubits), len(qc.qubits)+2)) + list(range(0, len(qc.qubits))), range(0, len(qc.clbits)))

# nested if +5
qc_new.x(b[2])

qc_new.x(anc[1])

qc = QuantumCircuit(b, x, name="cc+5")
add(qc, b, x, 3)

qc_ctrl = qc.to_gate().control(2)

qc_new.append(qc_ctrl, list(range(len(qc.qubits), len(qc.qubits)+2)) + list(range(0, len(qc.qubits))), range(0, len(qc.clbits)))

# controlled +6
qc_new.x(b[0])
qc_new.x(b[1])

qc_new.x(anc[0])

qc = QuantumCircuit(b, x, name="c+6")
add(qc, b, x, 3)

qc_ctrl = qc.to_gate().control(1)
qc_ctrl_inv = qc_ctrl.inverse()

qc_new.append(qc_ctrl, list(range(len(qc.qubits), len(qc.qubits)+1)) + list(range(0, len(qc.qubits))), range(0, len(qc.clbits)))

qc_new.cx(x[3], anc[2])

qc_new.append(qc_ctrl_inv, list(range(len(qc.qubits), len(qc.qubits)+1)) + list(range(0, len(qc.qubits))), range(0, len(qc.clbits)))

# nested if +5
qc_new.x(b[0])
qc_new.x(b[1])

qc = QuantumCircuit(b, x, name="cc+5")
add(qc, b, x, 3)

qc_ctrl = qc.to_gate().control(2)

qc_new.append(qc_ctrl, list(range(len(qc.qubits), len(qc.qubits)+3, 2)) + list(range(0, len(qc.qubits))), range(0, len(qc.clbits)))

qc_new.cx(x[3], anc[2])

from collections import defaultdict
counts = defaultdict(int)

# print(qc_new)
qc_new.measure(x, cx)


# Simulate the circuit.
simulator = AerSimulator()
qct = transpile(qc_new, simulator)
# print(qc_new)

result = Aer.get_backend('statevector_simulator').run(qct, shots=1000).result()
counts = result.get_counts()
# print(counts)
integer_dict = {int(key, 2): value for key, value in counts.items()}

print(integer_dict)
