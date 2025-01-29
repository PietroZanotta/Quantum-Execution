from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, transpile
from qiskit_aer import AerSimulator, Aer
from QArithmetic import mult, cqft

depth_list =[]

m=23

for n in range(3, m):
# Registers and circuit.
    a = QuantumRegister(n)
    b = QuantumRegister(n)
    m = QuantumRegister(2*n)
    cm = ClassicalRegister(2*n)
    qc = QuantumCircuit(a, b, m, cm)

    mult(qc, a, b, m, n-1)

    # print(qc)
    # print(n)
    # print(qc.depth())
    # print((n*(n+1)/2 + 2*(5*n*(n-1)/2 + n) -n+2)*(n-1)-(n-2)== qc.depth())
    # depth_list.append(qc.depth())
    print(qc.size())
#     # print("\n")

# print(qc)
# print("true size: " + str(qc.size()))


def qft_size(a):
    return (a*n)**2 + a*n - a*n*(a*n+1)/2

def cqft_size(a, n):
    return a*(n)**2 + n - a*n*(n+1)/2

n=4
print(int((2*(n-1))*(cqft_size(5, n))+ (n-1)*(qft_size(1))))

# qc = QuantumCircuit(a, cm)
# cqft(qc, 0, a[1::], n-1)
# print("true size: " + str(qc.size()))
# print(int((cqft_size(5, n-1))))

# print(qc)


# gate_counts = qc.count_ops()
# print(gate_counts)

# one_qubit_gates = sum(count for gate, count in gate_counts.items() if gate in ["h", "x", "y", "z", "s", "t"])
# multi_qubit_gates = sum(count for gate, count in gate_counts.items() if gate in ["cx", "ch", "mcphase", "cz", "cp", "swap", "ccx"])

# print(f"One-qubit gates: {one_qubit_gates}")
# print(f"Multi-qubit gates: {multi_qubit_gates}")

# print(multi_qubit_gates + one_qubit_gates)