from qiskit_aer.noise import NoiseModel
from qiskit.providers.fake_provider import GenericBackendV2
from qiskit_aer import Aer, AerSimulator
from qiskit_aer.primitives import Estimator as AerEstimator, Sampler as AerSampler
from qiskit_algorithms.utils import algorithm_globals
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, transpile
from QArithmetic import mult


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


a = QuantumRegister(2)
b = QuantumRegister(2)
m = QuantumRegister(4)
cm = ClassicalRegister(4)
qc = QuantumCircuit(a, b, m, cm)

# Numbers to multiply.
qc.x(a[1]) # a = 10
qc.h(b[0]) # b = 10 / 11
qc.x(b[1])

# Multiply the numbers, so |a>|b>|m=0> to |a>|b>|a*b>.
mult(qc, a, b, m, 2)

# Measure the result.
qc.measure(m, cm)

job = sampler.run(qc, shots=128)

dists = job.result().quasi_dists

counts = {key: int(value * 128) for key, value in dists[0].items()}
print(counts)