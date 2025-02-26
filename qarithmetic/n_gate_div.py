from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, transpile
from qiskit_aer import AerSimulator, Aer
from QArithmetic import div

n=4

# Registers and circuit.
a = QuantumRegister(2*n)
b = QuantumRegister(2*n)
c = QuantumRegister(n)
ca = ClassicalRegister(2*n)
cb = ClassicalRegister(2*n)
cc = ClassicalRegister(n)
qc = QuantumCircuit(a,b,c,ca,cb,cc)

div(qc, b, a, c, n)

print("true size: " + str(qc.size()))


def qft_size(a):
    return (a*n)**2 + a*n - a*n*(a*n+1)/2


def cqft_size(a, n):
    return a*(n)**2 + n - a*n*(n+1)/2


def cadd_size(n):
    return int((2*(n-1))*(cqft_size(5, n))+ (n-1)*(qft_size(1)))


def add_size(n):
    return int(2*(0-n*(n+1)/2 + n**2 + n) + n**2 +n - n*(n+1)/2)

print(int(n*(4*n + add_size(2*n) + 5 + 2*cqft_size(5, 2*n) + qft_size(2) + 2*n-1 )))
# print(qc.depth())

# gate_counts = qc.count_ops()
# print(gate_counts)

# one_qubit_gates = sum(count for gate, count in gate_counts.items() if gate in ["h", "x", "y", "z", "s", "t"])
# multi_qubit_gates = sum(count for gate, count in gate_counts.items() if gate in ["cx", "ch", "mcphase", "cz", "cp", "swap", "ccx"])

# print(f"One-qubit gates: {one_qubit_gates}")
# print(f"Multi-qubit gates: {multi_qubit_gates}")

# # print(multi_qubit_gates + one_qubit_gates)