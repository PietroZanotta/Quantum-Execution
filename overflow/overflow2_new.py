
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
from qiskit import QuantumCircuit, QuantumRegister, transpile, ClassicalRegister
from qiskit.circuit.library import QFT, SGate, SdgGate, TGate, TdgGate, CPhaseGate
import matplotlib.pyplot as plt
from qiskit_aer import AerSimulator, Aer
from fpqs import fpqs_circ
from QArithmetic import add, sub, cadd


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
    x = QuantumRegister(digits)
    three_or_one = QuantumRegister(digits)
    anc = QuantumRegister(3)
    cx = ClassicalRegister(digits)

    qc = QuantumCircuit(x, three_or_one, anc)
    def oracle(qc, num_qubit):
        # +3
        qc.x(three_or_one[0:2]) # 0011
        qc_ = QuantumCircuit(x, three_or_one)
        add(qc_, three_or_one, x, digits-1)
        qc_dagger = qc_.inverse()

        qc.append(qc_, list(x) + list(three_or_one))
        qc.cx(x[3], anc[0])
        qc.append(qc_dagger, list(x) + list(three_or_one))

        # controlled +1 and its inverse
        qc.x(three_or_one[1])

        qc_ = QuantumCircuit(x, three_or_one)
        add(qc_,three_or_one, x, digits-1)
        qc_dagger = qc_.inverse()

        qc.append(qc_, list(x) + list(three_or_one))
        qc.cx(x[3], anc[2])
        qc.append(qc_dagger, list(x) + list(three_or_one))

    # A is state preparation metric
    A = QuantumCircuit(x, three_or_one, anc)

    # init
    A.h(x[0:3]) # 0abc

    # Perform fixed-point quantum search
    fpqs_qc = fpqs_circ(oracle, .5, 4, A, 10, x, n_iter)
    print(fpqs_qc)
    A.append(fpqs_qc, range(len(A.qubits)))

    # Measure the x
    A.measure_all()

    # Run the simulation
    qct = transpile(A, simulator)

    result = Aer.get_backend('statevector_simulator').run(qct, shots=n_shots).result()
    counts = result.get_counts()
    summed_counts = {}

    for key, value in counts.items():
        last_4_bits = key[-4:]  
        if last_4_bits in summed_counts:
            summed_counts[last_4_bits] += value 
        else:
            summed_counts[last_4_bits] = value 

    print(counts)
    print(summed_counts)
    counts = summed_counts

    # Post processing
    decimal_list = [int(reversed_key, 2) for reversed_key in counts.keys()]
    digit_dict = {int(key, 2): value for key, value in counts.items()}
    print(digit_dict)
    
    # Plot the frequencies
    if plot == True:
        plt.figure(figsize=(10, 5))
        plt.bar(counts.keys(), counts.values())
        plt.xlabel('States')
        plt.ylabel('Frequency')
        plt.xticks(rotation=90)
        plt.tight_layout()
        plt.show()

    return(counts)

simulate_classical_circ(n_shots=100, n_iter=9)
