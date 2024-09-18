# vannila version but the circuit being in the oracle

'''

Immagining a classical program s.t.

if x >= 5:
    return x+1
else:
    return x

The following quantum circuit finds the values of x that can cause a potential overflow in the above classical program,
assuming the program is run on a 3-bit machine, using fixed-point quantum search algorithm.

'''

import math
import itertools
import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, transpile
from qiskit.circuit.library import QFT, SGate, SdgGate, TGate, TdgGate, CPhaseGate
import matplotlib.pyplot as plt
from qiskit_aer import AerSimulator, Aer
from fpqs2 import fpqs_circ
from utils import *


import math
import numpy as np
from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
from qiskit_aer import AerSimulator

# Run the simulation
simulator = AerSimulator()
digits = 4

def encoding(qc):
    '''
        Encoding the numbers of interest in the classical program in the circuit 
        
        Parameters:
            qc (QuantumCircuit): quantum circuit where the numbers should be encoded

        Returns:
            QuantumCircuit: the quantum circuit with the encoded numbers
    '''
    # Encoding x as an equal superposition of values ranging from 0 to 7
    qc.h(range(1, 4)) 
    
    # Encoding 3 (0011). 3 comes from 2^3 - 1 - 5 
    # where 2^3 - 1 is maximum number the 3-bits machine can represent and 5 is part of the if statement
    qc.x(6)             
    qc.x(7)

    # Encoding 1 (0001) for performing a controlled +1 as in the classical program
    qc.x(11)

    return qc


def prep_circuit():
    qc = QuantumCircuit(2*digits + 1, digits, name="+")

    return qc


def oracle(qc, digits=3):
    # Oracle for the fpqs. Contains the logic of the classical program

    # Initialization
    circuit = QuantumCircuit(3*(digits+1) + 3, (digits+1))
    
    # +3
    add3 = quantum_addition(prep_circuit, (digits+1))
    circuit.append(add3, range(0, 9), range(0,4))

    # Cnot the sign qubit of x+3 to the first ancilla
    circuit.cx(4, 12)

    # Invert the +3
    circuit.append(add3.inverse(), range(0, 9), range(0, 4))

    # Controlled +1
    ctrl_qadd = controlled_quantum_addition(prep_circuit, (digits+1), 8)
    ranges = [range(0, 4), range(8, 13)]
    range_add_1 = list(itertools.chain(*ranges))
    circuit.append(ctrl_qadd, range_add_1, range(0, 4))

    # Cnot the sign qubit of x+1 to the second ancilla
    circuit.cx(8, 13)
    qc.barrier()
    
    inv_circuit = circuit.inverse()

    # The oracle is B, cnot, B_dagger, where B is the circuit implementing the classical circuit logic 
    
    # Append B
    qc.append(circuit, range(0,15), range(0,4))
    
    # Cnot the second ancilla to the third ancilla 
    qc.cx(13, 14)
    
    # Append B_dagger
    qc.append(inv_circuit, range(0,15), range(0,4))


def simulate_classical_circ(n_shots=100):
    '''
        Simulate the classical circuit and returns any x thay could cause the overflow, while plotting the result
        of the simulations

        Parameters:
            n_shots (int): number of times the simulation is performed
    '''

    simulator = AerSimulator()
    digits = 4

     # Create the circuit
    fpqs_qc = fpqs_circ(oracle, .5, 15, digits, encoding, 5)
    fpqs_qc.barrier()

    # Measure the x at the end of the circuit
    fpqs_qc.measure(range(0, 4), reversed(range(0, 4)))

    # Run the simulation
    qct = transpile(fpqs_qc, simulator)
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