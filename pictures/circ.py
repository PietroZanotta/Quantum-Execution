from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library import HGate

qr_x = QuantumRegister(4, 'x')
qr_3 = QuantumRegister(4, '3')
qr_y = QuantumRegister(4, 'y')
qr_1 = QuantumRegister(4, '1')
qr_control = QuantumRegister(2, 'control')

qc = QuantumCircuit(qr_3, qr_x, qr_1, qr_y, qr_control)



# Drawing the circuit
from qiskit.visualization import circuit_drawer
circuit_drawer(qc, output='mpl',fold=20,cregbundle=False, wire_order=[*qr_x,*qr_y,cr_control]) #mpl for matplotlib