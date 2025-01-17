import math
import itertools
import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, transpile, ClassicalRegister
from qiskit.circuit.library import QFT, SGate, SdgGate, TGate, TdgGate, CPhaseGate
import matplotlib.pyplot as plt
from qiskit_aer import AerSimulator, Aer
from fpqs import fpqs_circ
from QArithmetic import add, sub, cadd

from overflow1_new import simulate_classical_circ as sim1
from overflow2 import simulate_classical_circ as sim2
from overflow3_new import simulate_classical_circ as sim3
from overflow4 import simulate_classical_circ as sim4
from overflow_mod import simulate_classical_circ as simMod
from overflow_mult import simulate_classical_circ as simMult
from overflow_div import simulate_classical_circ as simDiv

# # 1: 95
# sim1(n_shots=100)

# # 2: 99
# sim2(n_shots=100)

# # 3: 98
# sim3(n_shots=100)

# # 4: 94
# sim4(n_shots=100)

# mod:
# simMod(n_shots=100)

# mult: 95
# simMult(n_shots=100)

# div: 94
simDiv(n_shots=100)