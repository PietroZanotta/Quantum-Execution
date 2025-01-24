from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, transpile
from qiskit_aer import AerSimulator, Aer
from QArithmetic import add, qft, bitwise_and


n = 20

a = QuantumRegister(n)
b = QuantumRegister(n)
cb = ClassicalRegister(n)
qc = QuantumCircuit(a, b, cb)

add(qc, a, b, n-1)


print(qc)
print(qc.depth())
print(n*5 -2)

# print(qc)
# print(qc.size())

# print(int(2*(0-n*(n+1)/2 + n**2 + n) + n**2 +n - n*(n+1)/2))

# gate_counts = qc.count_ops()
# print(gate_counts)

# one_qubit_gates = sum(count for gate, count in gate_counts.items() if gate in ["h", "x", "y", "z", "s", "t"])
# multi_qubit_gates = sum(count for gate, count in gate_counts.items() if gate in ["cx", "cz", "cp", "swap", "ccx"])

# print(f"One-qubit gates: {one_qubit_gates}")
# print(f"Multi-qubit gates: {multi_qubit_gates}")
