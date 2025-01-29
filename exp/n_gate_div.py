from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, transpile
from qiskit_aer import AerSimulator, Aer
from QArithmetic import div

m=7

def qft_size(a):
    return (a*n)**2 + a*n - a*n*(a*n+1)/2


def cqft_size(a, n):
    return a*(n)**2 + n - a*n*(n+1)/2


def cadd_size(n):
    return int((2*(n-1))*(cqft_size(5, n))+ (n-1)*(qft_size(1)))


def add_size(n):
    return int(2*(0-n*(n+1)/2 + n**2 + n) + n**2 +n - n*(n+1)/2)

for n in range(3, m):
    # Registers and circuit.
    a = QuantumRegister(2*n)
    b = QuantumRegister(2*n)
    c = QuantumRegister(n)
    ca = ClassicalRegister(2*n)
    cb = ClassicalRegister(2*n)
    cc = ClassicalRegister(n)
    qc = QuantumCircuit(a,b,c,ca,cb,cc)

    div(qc, b, a, c, n)

    # print(qc)
    # print(qc.depth())
    print(qc.size()==int(n*(4*n + add_size(2*n) + 5 + 2*cqft_size(5, 2*n) + qft_size(2) + 2*n-1 )))
    print(10*n**2 + (2*n-1) + 2*(n-1) - 3*(n-1)+3*n + n*(2*n*(2*n+1)/2 + 2*(5*2*n*(2*n-1)/2 + 2*n) -2*n+2) + 1)
    print(10*n**2 + (2*n-1) + 2*(n-1) - 3*(n-1)+3*n + n*(2*n*(2*n+1)/2 + 2*(5*2*n*(2*n-1)/2 + 2*n) -2*n+2) + 1 == qc.depth())
    print("\n")


# print("true size: " + str(qc.size()))

n=64
print(10*n**2 + (2*n-1) + 2*(n-1) - 3*(n-1)+3*n + n*(2*n*(2*n+1)/2 + 2*(5*2*n*(2*n-1)/2 + 2*n) -2*n+2) + 1)

# print(int(n*(4*n + add_size(2*n) + 5 + 2*cqft_size(5, 2*n) + qft_size(2) + 2*n-1 )))

# gate_counts = qc.count_ops()
# print(gate_counts)

# one_qubit_gates = sum(count for gate, count in gate_counts.items() if gate in ["h", "x", "y", "z", "s", "t"])
# multi_qubit_gates = sum(count for gate, count in gate_counts.items() if gate in ["cx", "ch", "mcphase", "cz", "cp", "swap", "ccx"])

# print(f"One-qubit gates: {one_qubit_gates}")
# print(f"Multi-qubit gates: {multi_qubit_gates}")

# # print(multi_qubit_gates + one_qubit_gates)