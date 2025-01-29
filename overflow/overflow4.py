# sum of a superposition and controlled +1 and +7 at the end

'''

Immagining a classical program s.t.

if x >= sup(3, 4):
    return x+1
else:
    return x+7

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
from fpqs4 import fpqs_circ
from utils import *
from qiskit.quantum_info import Statevector


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

    qc = QuantumCircuit(4*(digits+1) + 2, (digits+1)) # 3 numbers + 2 ancilla

    # Encoding 7 (0111)
    qc.barrier()
    qc.x(range(1, 4))
    
    # Encode the sqrt(3/4) 0011 + 1/2 0100
    theta = 2 * math.pi / 3  
    qc.ry(theta, 4)    

    qc.cx(4, 5)  
    qc.cx(4, 6) 

    qc.x(6) 

    qc.swap(4, 7)
    qc.swap(5, 6)

    # Encoding 1 (0001) for performing a controlled +1 as in the classical program
    qc.x(11)

    # Encoding x as an equal superposition of values ranging from 0 to 7
    qc.h(range(13, 16)) 

    return qc


def simulate_classical_circ(n_shots=100, n_iter=None, plot=True):
    '''
        Simulate the classical circuit and returns any potential overflow, while plotting the result
        of the simulations

        Parameters:
            n_shots (int): number of times the simulation is performed
            n_iter (int): number of times the fpqs iterator runs
    '''

    simulator = AerSimulator()
    digits = 4

    # Initialization
    qc = encoding()

    # +3
    add3 = quantum_addition(prep_circuit, digits)
    ranges = [range(4, 8), range(12, 17)]
    range_add_3 = list(itertools.chain(*ranges))

    qc.append(add3, range_add_3, range(0, 4))

    # Cnot the sign qubit of x+3 to the first ancilla
    qc.cx(12, 16)

    # Invert the +3
    qc.append(add3.inverse(), range_add_3, range(0, 4))
 
    # Controlled +1
    ctrl_qadd = controlled_quantum_addition(prep_circuit, digits, 8)
    ranges = [range(8, 12), range(12, 17)]
    range_add_1 = list(itertools.chain(*ranges))

    qc.append(ctrl_qadd, range_add_1, range(0, 4))

    # Controlled +7
    qc.barrier()
    qc.x(16)

    ctrl_qadd = controlled_quantum_addition(prep_circuit, digits, 8)
    ranges = [range(0, 4), range(12, 17)]
    range_add_7 = list(itertools.chain(*ranges))

    qc.append(ctrl_qadd, range_add_7, range(0, 4))

    # Apply fixed point quantum search to the last 4th qubit
    def oracle(circuit, num_qubits):
        # Oracle for the fpqs. If sign integer of x after everything is 1 (i.e. a overflow happened) -> 1, otherwise 0
        qc.barrier()
        circuit.cx(12, 17)

    qc.barrier()

    # A is state preparation metric
    A = qc

    # Perform fixed-point quantum search
    fpqs_qc = fpqs_circ(oracle, .5, 4, A, n_iter)

    qc.append(fpqs_qc, range(0, 18), range(0,4))

    # Measure the 4, 5, 6, 7 qubits
    qc.barrier()
    qc.measure(range(12, 16), reversed(range(0, 4)))

    # Run the simulation
    seed_transpiler = 42
    qct = transpile(qc, simulator, seed_transpiler=seed_transpiler)
    seed_simulator = 42
    backend = Aer.get_backend('statevector_simulator')

    result = backend.run(qct, shots=n_shots, seed_simulator=seed_simulator).result()    
    counts = result.get_counts()

    print(counts)

    return(counts)

    # Post processing
    decimal_list = [int(reversed_key, 2) for reversed_key in counts.keys()]
    digit_dict = {int(key, 2): value for key, value in counts.items()}
    # print(digit_dict)
    
    # Plot the frequencies
    if plot==True:
        plt.figure(figsize=(10, 5))
        plt.bar(counts.keys(), counts.values())
        plt.xlabel('States')
        plt.ylabel('Frequency')
        plt.xticks(rotation=90)
        plt.tight_layout()
        plt.show()


# simulate_classical_circ()
