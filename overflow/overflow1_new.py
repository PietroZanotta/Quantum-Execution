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
    anc = QuantumRegister(2)
    cx = ClassicalRegister(digits)

    qc = QuantumCircuit(x, three_or_one, anc)

    # init
    qc.x(three_or_one[0:2]) # 0011
    qc.h(x[0:3]) # 0abc

    # +3
    qc_ = QuantumCircuit(x, three_or_one)
    add(qc_, three_or_one, x, digits-1)
    qc_dagger = qc_.inverse()

    qc.append(qc_, list(x) + list(three_or_one))
    qc.cx(x[3], anc[0])
    qc.append(qc_dagger, list(x) + list(three_or_one))

    # controlled +1
    qc.x(three_or_one[1])
    cadd(qc, anc[0], three_or_one, x, digits-1)

    # Apply fixed point quantum search to the last 4th qubit
    def oracle(circuit, num_qubits):
        # Oracle for the fpqs. If the sign integer of x+1 is 1 (i.e. a overflow happened) -> 1, otherwise 0
        circuit.barrier()
        circuit.cx(3, 9)

    # A is state preparation metric
    A = qc

    # Perform fixed-point quantum search
    fpqs_qc = fpqs_circ(oracle, .5, 4, A, 9, x, n_iter)
    # print(fpqs_qc)
    qc.append(fpqs_qc, range(len(A.qubits)))

    # Measure the x
    qc.measure_all()

    # Run the simulation
    seed_transpiler = 42
    qct = transpile(qc, simulator, seed_transpiler=seed_transpiler)
    seed_simulator = 42
    backend = Aer.get_backend('statevector_simulator')

    result = backend.run(qct, shots=n_shots, seed_simulator=seed_simulator).result()
    counts = result.get_counts()
    summed_counts = {}

    for key, value in counts.items():
        last_4_bits = key[-4:]  
        if last_4_bits in summed_counts:
            summed_counts[last_4_bits] += value 
        else:
            summed_counts[last_4_bits] = value 

    # print(counts)
    print(summed_counts)
    counts = summed_counts

    # Post processing
    decimal_list = [int(reversed_key, 2) for reversed_key in counts.keys()]
    digit_dict = {int(key, 2): value for key, value in counts.items()}
    # print(digit_dict)
    
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

# simulate_classical_circ(n_shots=100, n_iter=5)
