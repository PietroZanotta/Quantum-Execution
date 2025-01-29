from overflow_mult import simulate_classical_circ as simMult

for i in range(1, 10): 
    simMult(n_shots=100, n_iter=i)