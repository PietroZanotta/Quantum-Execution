from overflow_div import simulate_classical_circ as simDiv

for i in range(1, 10): 
    simDiv(n_shots=100, n_iter=i)