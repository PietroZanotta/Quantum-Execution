"""
if x/(2 or 3) >= 2:
    return x+2
else:
    return x+5
"""

from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, transpile
from qiskit_aer import AerSimulator, Aer
from fpqs6 import fpqs_circ
import matplotlib.pyplot as plt
from QArithmetic import div, add, cadd

def simulate_classical_circ(n_shots=100, n_iter=None, plot=False):

    # Registers and circuit.
    b = QuantumRegister(6)
    x = QuantumRegister(6)
    m = QuantumRegister(3)
    anc = QuantumRegister(2)
    cm = ClassicalRegister(3)
    cb = ClassicalRegister(6)
    cx = ClassicalRegister(6)
    cc = ClassicalRegister(4)
    canc = ClassicalRegister(2)
    qc = QuantumCircuit(b, x, m, anc, cc)#, cx, cb, cm, canc)
    qc_new = QuantumCircuit(b, x, m, anc, cc)#, cx, cb, cm, canc)

    # Init
    qc_new.h(x[0]) # x = from 000 000 to 000 111 
    qc_new.h(x[1])
    qc_new.h(x[2])

    # # qc_new.x(x[0]) # x = from 000 000 to 000 111 
    # qc_new.x(x[0])
    # qc_new.x(x[2]) # 101 = 5

    qc_new.x(b[4]) # b = 010 000 / 011 000
    qc_new.h(b[3])


    # Divide the numbers, so |0...0 x⟩|b 0...0⟩|0...0⟩ → |x mod b 0...0⟩|b⟩|a/b⟩
    qc.barrier()
    div(qc, x, b, m, 3)
    qc.barrier()



    # Encode |6> in the last 3 qubits of b 
    # the state becomes |x mod b 000⟩|b 110⟩|0 a/b⟩ --> |x mod b 00 sign(x+6)⟩|b 110⟩|0 a/b⟩
    qc.x(b[1]) # 110
    qc.x(b[2]) 
    # qc.x(x[0]) 
    qc.barrier()

    # # m+6
    # # here m is using the first qubit of x to detect overflow 
    add(qc, b[0:3], [m[0], m[1], m[2], x[0]], 3)
    qc_inv = qc.inverse()
    qc_new.append(qc, range(0, len(qc.qubits)), range(0, len(qc.clbits)))


    # first ancilla qubit indicates if x/(2 or 3) >= 7
    # |x mod b 00 sign(d)⟩|b 101⟩|0 a/b⟩|0a1⟩
    qc_new.barrier()
    qc_new.cx(x[0], anc[0])


    # revert the /(2 or 3) and +1
    # |x mod b 00 sign(d)⟩|b 101⟩|0 a/b⟩|0a1⟩ --> |000x⟩|b 000⟩|000⟩|0a1⟩ 
    qc_new.append(qc_inv, range(0, len(qc.qubits)), range(0, len(qc.clbits)))

    # controlled x+2 based on a1
    # x is here considerend as |00sign(x)x⟩
    # hence |000x⟩|b 000⟩|000⟩|0a1⟩  --> |00 (x+2)⟩|b 000⟩|0 10⟩|0a1⟩ 
    qc_new.x(m[1]) # 010 # encode 2 in m
    cadd(qc_new, anc[0], m, [x[0], x[1], x[2], x[3]], 3)

    # x gate to the first ancilla to act on the other qubits
    qc_new.x(anc[0])

    # encode |5⟩ in m 
    # hence |00 (x+2)⟩|b 000⟩|0 11⟩|0a1⟩ --> |00 (x+5)⟩|b 000⟩|101⟩|0a1⟩
    qc_new.x(m[1]) # 101 # encode 5 in m
    qc_new.x(m[2])
    qc_new.x(m[0])

    # controlled x+5
    cadd(qc_new, anc[0], m, [x[0], x[1], x[2], x[3]], 3)

    # fpqs to amplify the x[3] qubit
    def oracle(qc, num_qubits):
        # oracle to observe if an overflow happened
        qc.cx(9, 16)

    A = qc_new

    # Perform fixed-point quantum search
    fpqs_qc = fpqs_circ(oracle, .5, 4, A, 3)
    qc_new.append(fpqs_qc, range(0, 17), range(0, 4))

    # Measure the result
    qc_new.barrier()
    # qc_new.measure(m, cm)
    # qc_new.measure(b, cb)
    # qc_new.measure(anc, canc)
    # qc_new.measure(reversed([x[3], x[2], x[1], x[0]]), cc)

    qc_new.measure_all()

    # qc_new.measure(x, cx)

    # Simulate the circuit.
    simulator = AerSimulator()
    qct = transpile(qc_new, simulator)
    # print(qct)

    result = Aer.get_backend('statevector_simulator').run(qct, shots=100).result()
    counts = result.get_counts()
    # print(counts)
    # decimal_dict = {int(key, 2): value for key, value in counts.items()}

    # sorted_dict = dict(sorted(decimal_dict.items()))

    # print(sorted_dict)

    # print(sum(counts.values()))

    new_dict={}

    for key, value in counts.items():
        new_key = key[7:-11]  # Remove the first 7 and last 6 bits

        if new_key in new_dict:
            new_dict[new_key] += value  # Sum the values if the key already exists
        else:
            new_dict[new_key] = value 

    # Print the new dictionary
    print(new_dict)

    if plot == True:
        plt.figure(figsize=(10, 5))
        plt.bar(counts.keys(), counts.values())
        plt.xlabel('States')
        plt.ylabel('Frequency')
        plt.xticks(rotation=90)
        plt.tight_layout()
        # plt.show()