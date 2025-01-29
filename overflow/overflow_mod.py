"""
if x mod 2 == 0:
    return x/2
else:
    return x*3 + 1
"""

from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, transpile
from qiskit_aer import AerSimulator, Aer
from fpqs7 import fpqs_circ
import matplotlib.pyplot as plt
from QArithmetic import div, add, cadd, mult


def simulate_classical_circ(n_shots=100, n_iter=None, plot=False):
    # Registers and circuit.
    b = QuantumRegister(6)
    x = QuantumRegister(6)
    m = QuantumRegister(3)
    anc = QuantumRegister(2)
    cm = ClassicalRegister(3)
    cb = ClassicalRegister(6)
    cx = ClassicalRegister(6)
    cc = ClassicalRegister(6)
    canc = ClassicalRegister(2)
    qc = QuantumCircuit(b, x, m, anc)# cc, cx, cb, cm, canc)
    qc_new = QuantumCircuit(b, x, m, anc, cx)#, cb, cm, canc, cc)#cc, cx, cb, cm, canc)

    # Init
    qc_new.h(x[0]) # x = from 000 000 to 000 111 
    qc_new.h(x[1])
    qc_new.h(x[2])


    # qc_new.x(x[1]) # 2 or 3
    # qc_new.h(x[0])

    qc_new.x(b[4]) # b = 010 000 
    qc_new.x(b[3])

    # Divide the numbers, so |0...0 x⟩|b 0...0⟩|0...0⟩ → |x mod b 0...0⟩|b⟩|x/b⟩
    div(qc, x, b, m, 3)

    # Verify if x mod 2 == 0 and mark it in the first ancilla
    qc_inv = qc.inverse()
    qc_new.append(qc, range(0, len(qc.qubits)), range(0, len(qc.clbits)))

    qc_new.x(x[3:6])
    qc_new.mcx([x[4], x[5], x[3]], anc[0])
    qc_new.x(x[3:6])
    qc_new.barrier()

    # revert the /2
    qc_new.append(qc_inv, range(0, len(qc.qubits)), range(0, len(qc.clbits)))

    # controlled x/2 based on a1
    qc = QuantumCircuit(b, x, m)# cc, cx, cb, cm, canc)
    div(qc, x, b, m, 3)
    div2 = qc.to_gate().control(1)

    qc_new.append(div2, [anc[0]]+list(range(0, len(qc.qubits))), range(0, len(qc.clbits)))

    # x gate to the first ancilla to act on the other qubits
    qc_new.x(anc[0])

    # encode |3⟩ in b 
    qc_new.x(b[3])

    # controlled x*3 stored in x[3:5] + b[0:2]
    qc = QuantumCircuit(b, x)
    mult(qc, b[3:6], x[0:3], x[3:6] + b[0:3], 3)
    mult3 = qc.to_gate().control(1)

    qc_new.append(mult3, [anc[0]]+list(range(0, len(qc.qubits))), range(0, len(qc.clbits)))


    # encode |1⟩ in b 
    qc_new.x(b[4])

    # controlled x+1
    cadd(qc_new, anc[0],  b[3:6], x[3:6] + b[0:3], 4)

    # # qc.barrier()
    # # qc_new.x(b[0:3])
    # # qc_new.mcx(list(b[0:3]), 16)
    # # qc_new.x(b[0:3])
    # # qc_new.x(16)
    # # qc.barrier()

    # qc_new.x(range(0,3))
    # qc_new.mcx(list(range(0,3)), 16)
    # qc_new.x(range(0,3))
    # qc_new.x(16)

    # print(qc_new)

    # fpqs to amplify the x[3] qubit (/2 doesn't result in overflow)
    def oracle(qc, num_qubits):
        # oracle to observe if an overflow happened
        # qc.x(range(0,3))
        # qc.mcx(range(0,3), 16)
        qc.x(range(0,3))
        qc.mcx(list(range(0,3)), 16)
        qc.x(range(0,3))
        qc.x(16)

    A = qc_new

    # Perform fixed-point quantum search
    fpqs_qc = fpqs_circ(oracle, .5, 4, A, n_iter)
    qc_new.append(fpqs_qc, range(0, 17), range(0, 6))

    # Measure the result
    # qc_new.barrier()
    # qc_new.measure(m, cm)
    # qc_new.measure(b, cb)
    # qc_new.measure(anc, canc)
    # # qc_new.measure(reversed([x[3], x[2], x[1], x[0]]), cc)
    # qc_new.measure(x, cx)

    qc_new.measure(x[3:6] + b[0:3], cx)

    # Simulate the circuit.
    simulator = AerSimulator()
    seed_transpiler = 42
    qct = transpile(qc_new, simulator, seed_transpiler=seed_transpiler)
    seed_simulator = 42
    backend = Aer.get_backend('statevector_simulator')

    result = backend.run(qct, shots=n_shots, seed_simulator=seed_simulator).result()
    counts = result.get_counts()
    print(counts)
    # decimal_dict = {int(key, 2): value for key, value in counts.items()}

    # sorted_dict = dict(sorted(decimal_dict.items()))

    # print(sorted_dict)

    if plot == True:

        plt.figure(figsize=(10, 5))
        plt.bar(counts.keys(), counts.values())
        plt.xlabel('States')
        plt.ylabel('Frequency')
        plt.xticks(rotation=90)
        plt.tight_layout()
        plt.show()

    return counts