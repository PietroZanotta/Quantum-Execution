import math
import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, transpile
from qiskit.circuit.library import QFT, SGate, SdgGate, TGate, TdgGate, CPhaseGate

def qft(circuit, qubits_range):
    # compute QFT
    for tar in qubits_range:
        circuit.h(tar)
        for contr in range(tar+1, np.max(qubits_range)+1):
            circuit.cp(2*math.pi/(2**(contr - tar + 1)), contr, tar)
        circuit.barrier()


def controlled_qft(circuit, ctrl, qubits_range):
    # compute controlled QFT
    for tar in qubits_range:
        circuit.ch(ctrl, tar)
        for contr in range(tar+1, np.max(qubits_range)+1):
            ctrl_cp = CPhaseGate(2*math.pi/(2**(contr - tar + 1))).control(1)
            circuit.append(ctrl_cp, [ctrl, contr, tar])
        circuit.barrier()


def iqft(circuit, qubits_range):
    #compute IQFT
    for tar in reversed(qubits_range):
        circuit.h(tar)
        for contr in reversed(range(np.min(qubits_range), tar)):
            # print(str(contr) + " su " + str(tar))
            circuit.cp(-2*math.pi/(2**(tar - contr + 1)), contr, tar)
        circuit.barrier()


def controlled_iqft(circuit, ctrl, qubits_range):
    #compute IQFT
    for tar in reversed(qubits_range):
        circuit.ch(ctrl, tar)
        for contr in reversed(range(np.min(qubits_range), tar)):
            ctrl_cp = CPhaseGate(-2*math.pi/(2**(tar - contr + 1))).control(1)
            circuit.append(ctrl_cp, [ctrl, contr, tar])
        circuit.barrier()


def quantum_addition(prep_circuit, digits):
    ''' 
        Adding two numbers encoded in the same number of qubits

        Parameters:
            prep_circuit (function): Function initializing the circuit
            digits (int): Number of digits encoding the values

        Returns:
            QuantumCircuit: the controlled addition circuit
    '''
    # Initialization
    circuit = prep_circuit()
    circuit.barrier()

    # QFT on the first number register
    qft(circuit, range(digits, 2*digits))
    circuit.barrier()


    qubits_range = range(int(len(circuit.qubits)/2), len(circuit.qubits))

    for tar in range(digits, digits*2):
        for contr in range(tar - digits, digits):
            circuit.cp(2*math.pi / (2**(digits - (tar - contr) + 1)), contr, tar)
        circuit.barrier()

    # IQFT on the first number register
    iqft(circuit, range(digits, 2*digits))

    return circuit


def controlled_quantum_addition(prep_circuit, digits, control):
    '''
        Implementing regular quantum addition but controlled by a qubit

        Parameters:
            prep_circuit (function): Function initializing the circuit
            digits (int): Number of digits encoding the values
            control (int): Index of the control qubit 

        Returns:
            QuantumCircuit: the controlled addition circuit
    '''
    circuit = prep_circuit()
    circuit.barrier()
    # QFT on the a register and the ancilla
    controlled_qft(circuit, control, range(digits, 2*digits))
    # qft(circuit, range(digits, 2*digits))
    circuit.barrier()

    qubits_range = range(int(len(circuit.qubits)/2), len(circuit.qubits))

    for tar in range(digits, digits*2):
        for contr in range(tar - digits, digits):
            ctrl_cp = CPhaseGate(2*math.pi / (2**(digits - (tar - contr) + 1))).control(1)
            circuit.append(ctrl_cp, [control, contr, tar])
        circuit.barrier()

    # # IQFT on the a register
    controlled_iqft(circuit, control, range(digits, 2*digits))
    # iqft(circuit, range(digits, 2*digits))
    return circuit


def controlled_quantum_subtraction(prep_circuit, digits, control):
    '''
        Implementing regular quantum addition but controlled by a qubit

        Parameters:
            prep_circuit (function): Function initializing the circuit
            digits (int): Number of digits encoding the values
            control (int): Index of the control qubit 

        Returns:
            QuantumCircuit: the controlled addition circuit
    '''
    circuit = prep_circuit()
    circuit.barrier()
    # QFT on the a register and the ancilla
    controlled_qft(circuit, control, range(digits, 2*digits))
    circuit.barrier()

    qubits_range = range(int(len(circuit.qubits)/2), len(circuit.qubits))

    for tar in range(digits, digits*2):
        for contr in range(tar - digits, digits):
            ctrl_cp = CPhaseGate(-2*math.pi / (2**(digits - (tar - contr) + 1))).control(1)
            circuit.append(ctrl_cp, [control, contr, tar])
        circuit.barrier()

    # # IQFT on the a register
    controlled_iqft(circuit, control, range(digits, 2*digits))
    return circuit
