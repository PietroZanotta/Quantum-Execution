from qiskit_aer.noise import NoiseModel
from qiskit.providers.fake_provider import GenericBackendV2
from qiskit_aer import Aer, AerSimulator
from qiskit_aer.primitives import Estimator as AerEstimator, Sampler as AerSampler
from qiskit_algorithms.utils import algorithm_globals
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, transpile
from QArithmetic import add


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


# print(noise_model)

a = QuantumRegister(2)
b = QuantumRegister(3)
cb = ClassicalRegister(3)
qc = QuantumCircuit(a, b, cb)

# Numbers to add.
# qc.x(a[1]) # a = 001
qc.x(a[0])
# qc.x(a[3])
qc.h(b[0]) # b = 011 / 010
qc.x(b[1])
# qc.x(b[3])

# Add the numbers, so |a>|b> to |a>|a+b>.
add(qc, a, b, 2)

# Measure the results.
qc.barrier()
qc.measure(b, cb)

job = sampler.run(qc, shots=128)

dists = job.result().quasi_dists

counts = {key: int(value * 128) for key, value in dists[0].items()}
print(counts)