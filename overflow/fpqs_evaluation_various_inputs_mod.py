from overflow_mod import simulate_classical_circ as simMod

for i in range(1, 10): 
    simMod(n_shots=100, n_iter=i)