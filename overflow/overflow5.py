import math
import itertools
import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, transpile
from qiskit.circuit.library import QFT, SGate, SdgGate, TGate, TdgGate, CPhaseGate
import matplotlib.pyplot as plt
from qiskit_aer import AerSimulator, Aer
from fpqs5 import fpqs_circ
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

    
    # Encoding 3 (0011). 3 comes from 2^3 - 1 - 5 
    # where 2^3 - 1 is maximum number the 3-bits machine can represent and 5 is part of the if statement
    qc.x(2)             
    qc.x(3)

    # Encoding 1 (0001) for performing a controlled +1 as in the classical program
    qc.x(7)
    # qc.x(10)
    # qc.x(13)

    # Encoding x as an equal superposition of values ranging from 0 to 7
    qc.h(range(9, 12)) 
    # qc.x(9)
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
    ranges = [range(0, 4), range(8, 13)]
    range_add_3 = list(itertools.chain(*ranges))
    add3 = quantum_addition(prep_circuit, digits)
    qc.append(add3, range_add_3, range(0, 4))

    # Cnot the sign qubit of x+3 to the first ancilla
    qc.cx(8, 12)


    # Invert the +3
    qc.append(add3.inverse(), range_add_3, range(0, 4))

    # Controlled +1
    ctrl_qadd = controlled_quantum_addition(prep_circuit, digits, 8)
    ranges = [range(4, 8), range(8, 13)]
    range_add_1 = list(itertools.chain(*ranges))
  

    qc.append(ctrl_qadd, range_add_1, range(0, 4))

    qc.cx(8, 13)

    # encode 5 in the first register
    qc.x(range(1,3))

    # encode 4 in the second register
    qc.x([5, 7])

    # Add 2 ancillas
    qc_new = QuantumCircuit(3*(digits) + 5, (digits))
    qc_new.append(qc, range(0, qc.num_qubits), range(0, digits)) 

    # controlled +5 on all the numbers but 8
    qc_new.x(13)


    ranges = [range(0, 4), range(8, 12), [13]]
    range_add_5 = list(itertools.chain(*ranges))
    add5 = controlled_quantum_addition(prep_circuit, digits, 8)
    qc_new.barrier()
    qc_new.barrier()
    qc_new.barrier()
    qc_new.barrier()
    qc_new.barrier()
    qc_new.barrier()
    qc_new.append(add5, range_add_5, range(0, 4))
    
    # in the first new ancilla store if x >= 3
    qc_new.cx(8, 14)

    # revert the controlled +5
    inv_add5 = controlled_quantum_addition(prep_circuit, digits, 8).inverse()
    qc_new.append(inv_add5, range_add_5, range(0, 4))

    # use the first new ancilla to do a controlled -4 to x >= 3
    # qc_new.x(14)
    ctrl_qsub = controlled_quantum_subtraction(prep_circuit, digits, 8)
    ranges = [range(4, 8), range(8, 12), [14]]
    range_sub_4 = list(itertools.chain(*ranges))

    qc_new.append(ctrl_qsub, range_sub_4, range(0, 4))

    # mark the overflow in the qubit 15
    qc_new.cx(8, 15)

    # reverse the controlled -4
    ctrl_qsub = controlled_quantum_subtraction(prep_circuit, digits, 8).inverse()

    qc_new.append(ctrl_qsub, range_sub_4, range(0, 4))
    
    qc_new.x(13)
       
    def oracle(circuit, num_qubits):
        circuit.barrier()
        # Oracle for the fpqs. Performs an or on the second or on the last qubits onto the first ancilla
        # circuit.ccx(13, 15, 16)
        # circuit.x([13, 15, 16])
        circuit.ccx(14, 15, 16) # 3 has 14 and 15 ancilla active
        circuit.mcx([12,13,14], 16) # 8 has 12,13,14 ancilla active
        # qc_new.z(1)
        circuit.barrier()


    # A is state preparation metric
    A = qc_new

    # Perform fixed-point quantum search
    fpqs_qc = fpqs_circ(oracle, .5, 4, A, n_iter)
    qc_new.append(fpqs_qc, range(0, 17), range(0,4))

    # qc.measure_all()
    qc_new.measure(range(8, 12), reversed(range(0,4)))
    # print(qct)

    # # # # Measure the x
    # # # ranges = [range(8, 12)]
    # # # # ranges = [range(4, 8)]
    # # # ranges = list(itertools.chain(*ranges))
    # # # qc.measure(ranges, reversed(range(0, 4)))

    # qc.measure_all()

    # Run the simulation
    # print("trans")
    seed_transpiler = 42
    qct = transpile(qc_new, simulator, seed_transpiler=seed_transpiler)
    seed_simulator = 42
    backend = Aer.get_backend('statevector_simulator')

    result = backend.run(qct, shots=n_shots, seed_simulator=seed_simulator).result()    
    counts = result.get_counts()

    # decimal_list = [int(reversed_key, 2) for reversed_key in counts.keys()]
    # digit_dict = {int(key, 2): value for key, value in counts.items()}
    # print(digit_dict)

    print(counts)
    
    # Plot the frequencies
    if plot == True:
        plt.figure(figsize=(10, 5))
        plt.bar(counts.keys(), counts.values())
        plt.xlabel('States')
        plt.ylabel('Frequency')
        plt.xticks(rotation=90)
        plt.tight_layout()
        # plt.show()
    
    return(counts)

# simulate_classical_circ(100)