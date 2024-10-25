from qiskit_aer.noise import NoiseModel
from qiskit.providers.fake_provider import GenericBackendV2
from qiskit_aer import Aer, AerSimulator
from qiskit_aer.primitives import Estimator as AerEstimator, Sampler as AerSampler
from qiskit_algorithms.utils import algorithm_globals
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, transpile
from QArithmetic import div

coupling_map = [(0, 1), (1, 2), (2, 3), (3, 4)]
device = GenericBackendV2(num_qubits=5, coupling_map=coupling_map, seed=54)

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

# Registers and circuit.
a = QuantumRegister(4)
b = QuantumRegister(4)
c = QuantumRegister(2)
ca = ClassicalRegister(4)
cb = ClassicalRegister(4)
cc = ClassicalRegister(2)
qc = QuantumCircuit(a,b,c,ca,cb,cc)

# Inputs.
qc.x(a[1]) # a = 0010 / 0011
qc.h(a[0])

qc.x(b[3]) # b = 1000

# Divide b by a.
div(qc, b, a, c, 2)

# Measure.
qc.barrier()
qc.measure(a, (ca))
qc.measure(b, cb)

qc.measure(c, (cc))

job = sampler.run(qc, shots=128)

dists = job.result().quasi_dists

counts = {key: int(value * 128) for key, value in dists[0].items()}
print(counts)

# exp:
# 00 0010 0011 
# 01 0000 0010

transpiled_circuit = transpile(qc, AerSimulator())
gate_count = transpiled_circuit.count_ops()
print(sum(gate_count.values()))