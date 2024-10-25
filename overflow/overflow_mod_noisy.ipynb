"""
if x mod 2 == 0:
    return x/2
else:
    return x*3 + 1
"""

from qiskit_aer.noise import NoiseModel
from qiskit.providers.fake_provider import GenericBackendV2
from qiskit_aer import Aer, AerSimulator
from qiskit_aer.primitives import Estimator as AerEstimator, Sampler as AerSampler
from qiskit_algorithms.utils import algorithm_globals
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, transpile
from fpqs7 import fpqs_circ
import matplotlib.pyplot as plt
from QArithmetic import div, add, cadd, mult

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
fpqs_qc = fpqs_circ(oracle, .5, 4, A, 6)
qc_new.append(fpqs_qc, range(0, 17), range(0, 6))

# Measure the result
# qc_new.barrier()
# qc_new.measure(m, cm)
# qc_new.measure(b, cb)
# qc_new.measure(anc, canc)
# # qc_new.measure(reversed([x[3], x[2], x[1], x[0]]), cc)
# qc_new.measure(x, cx)

qc_new.measure(x[3:6] + b[0:3], cx)

# Simulate the circuit
coupling_map = [(i, i + 1) for i in range(17)]
device = GenericBackendV2(num_qubits=18, coupling_map=coupling_map, seed=54)

seed = 170
algorithm_globals.random_seed = seed

noise_model = NoiseModel.from_backend(device)

sampler = AerSampler(
    backend_options={
        "method": "density_matrix",
        "coupling_map": coupling_map,
        "noise_model": noise_model,
    },
    run_options={"seed": seed, "shots": 1024},
    transpile_options={"seed_transpiler": seed},
)

job = sampler.run(qc_new, shots=128)

dists = job.result().quasi_dists

counts = {key: int(value * 128) for key, value in dists[0].items()}
print(counts)




plt.figure(figsize=(10, 5))
plt.bar(counts.keys(), counts.values())
plt.xlabel('States')
plt.ylabel('Frequency')
plt.xticks(rotation=90)
plt.tight_layout()
# plt.show()