# vanilla version

'''

Immagining a classical program s.t.

if x >= 5:
    return x+1
else:
    return x

The following quantum circuit seeks if a potential overflow caused by the program
on a 3-bit machine could happen using fixed-point quantum search algorithm.
If the overflow can happen, the measured state should be 1000. 
This program doesn't specify which x caused the overflow, to have that piece
of information run "overflow_detector2.py".

'''

import math
import itertools
import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, transpile
from qiskit.circuit.library import QFT, SGate, SdgGate, TGate, TdgGate, CPhaseGate
import matplotlib.pyplot as plt
from qiskit_aer import AerSimulator, Aer
from fpqs1 import fpqs_circ
from utils import *


def prep_circuit(digits = 3):
    qc = QuantumCircuit(2*(digits+1) + 1, (digits+1), name="+")

    return qc


def encoding(digits=3):
    '''
        Encoding the numbers of interest in the classical program in the circuit 
        
        Parameters:
            digits (int): number of digits representing the numbers in the circuit

        Returns:
            QuantumCircuit: the quantum circuit with the encoded numbers
    '''

    qc = QuantumCircuit(3*(digits+1) + 2, (digits+1)) # 3 numbers + 2 ancilla

    # Encoding x as an equal superposition of values ranging from 0 to 7
    qc.h(range(1, 4)) 
    
    # Encoding 3 (0011). 3 comes from 2^3 - 1 - 5 
    # where 2^3 - 1 is maximum number the 3-bits machine can represent and 5 is part of the if statement
    qc.x(6)             
    qc.x(7)

    # Encoding 1 (0001) for performing a controlled +1 as in the classical program
    qc.x(11)

    return qc


def simulate_classical_circ(n_shots=100):
    '''
        Simulate the classical circuit and returns any potential overflow, while plotting the result
        of the simulations

        Parameters:
            n_shots (int): number of times the simulation is performed
    '''

    simulator = AerSimulator()
    digits = 4

    # Initialization
    qc = encoding()

    # +3
    add3 = quantum_addition(prep_circuit, digits)
    qc.append(add3, range(0, 9), range(0, 4))

    # Cnot the sign qubit of x+3 to the first ancilla
    qc.cx(4, 12)

    # Invert the +3
    qc.append(add3.inverse(), range(0, 9), range(0, 4))

    # Controlled +1
    ctrl_qadd = controlled_quantum_addition(prep_circuit, digits, 8)
    ranges = [range(0, 4), range(8, 13)]
    range_add_1 = list(itertools.chain(*ranges))

    qc.append(ctrl_qadd, range_add_1, range(0, 4))

    # Apply fixed point quantum search to the last 4th qubit
    def oracle(circuit, num_qubits):
        # Oracle for the fpqs. If the sign integer of x+1 is 1 (i.e. a overflow happened) -> 1, otherwise 0
        qc.barrier()
        circuit.cx(8, 13)

    qc.barrier()

    # A is state preparation metric
    A = qc

    # Perform fixed-point quantum search
    fpqs_qc = fpqs_circ(oracle, .5, 4, A)

    qc.append(fpqs_qc, range(0, 14), range(0,4))

    # Measure the 4, 5, 6, 7 qubits
    qc.barrier()
    qc.measure(range(8, 12), reversed(range(0, 4)))

    # Run the simulation
    qct = transpile(qc, simulator)
    print(qct)

    result = Aer.get_backend('statevector_simulator').run(qct, shots=n_shots).result()
    counts = result.get_counts()

    print(counts)

    # Post processing
    # decimal_list = [int(reversed_key, 2) for reversed_key in counts.keys()]
    # digit_dict = {int(key, 2): value for key, value in counts.items()}
    # print(digit_dict)
    
    # Plot the frequencies
    plt.figure(figsize=(10, 5))
    plt.bar(counts.keys(), counts.values())
    plt.xlabel('States')
    plt.ylabel('Frequency')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()


simulate_classical_circ()
