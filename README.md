# Quantum Execution

Repository containing the code used for the evalutaion in [link to paper]. 

## Abstract

[Abstract of the paper]

## Code Structure

The repository is organized as follow:

 - [cbmc_unrolling](https://github.com/PietroZanotta/Quantum-Execution/tree/main/cbmc_unrolling): folder including a simple example how to use CBMC to unroll a C program
 - [exp](https://github.com/PietroZanotta/Quantum-Execution/tree/main/exp): folder containing scripts used to obtain the caracteristics (e.g. depth, number of gates) of some circuit representing arithmetic operation
 - [hybrid_method_metrics](https://github.com/PietroZanotta/Quantum-Execution/tree/main/hybrid_method_metrics):
    - [hybrid-fully_quantum_comparison](https://github.com/PietroZanotta/Quantum-Execution/tree/main/hybrid-fully_quantum_comparison): contains the unrolled porgrams used for the resource and performance comparison between the fully quantum execution and the hybrid execution
    - [symbolic_exec_quantum_comparison](https://github.com/PietroZanotta/Quantum-Execution/tree/main/symbolic_exec_quantum_comparison): contains some experimental evidence of the equivalence between Quantum Execution and Symbolic Execution on unrolled programs
 - [impact_input_on_fp](https://github.com/PietroZanotta/Quantum-Execution/tree/main/impact_input_on_fp): contains the programs used to study the impact of the input range on the FP rate
 - [largest_programs_metrics](https://github.com/PietroZanotta/Quantum-Execution/tree/main/largest_programs_metrics): contains the programs with the largest metrics (# of gates, depth, # of qubits) among the programs considered
 - [overflow](https://github.com/PietroZanotta/Quantum-Execution/tree/main/overflow): contains examples on using the Quantum Execution algorithm coupled with the Fixed Point Quantum Algorithm to find overflow occurring in simple programs
 - [qarithmetic](https://github.com/PietroZanotta/Quantum-Execution/tree/main/qarithmetic): contains the modified Quantum Arithmetics library
 - [quantum_sim_equivalence](https://github.com/PietroZanotta/Quantum-Execution/tree/main/quantum_sim_equivalence): contains the programs used to show the equivalence between our quantum simulator and quantum execution on Qiskit
 - [sv-benchmarks](https://github.com/PietroZanotta/Quantum-Execution/tree/main/sv-benchmarks): contains the modified used as benchmark. Such programs are a modified version of some programs provided by the [SV-Benchmarking](https://gitlab.com/sosy-lab/benchmarking/sv-benchmarks/-/tree/main/c?ref_type=heads) repository 
 - [vra_methods_comparison](https://github.com/PietroZanotta/Quantum-Execution/tree/main/vra_methods_comparison): contains the scripts comparing the performance in terms of FP and FN rate of [Angr](https://docs.angr.io/en/latest/core-concepts/symbolic.html), [CBMC (GOTO)](https://diffblue.github.io/cbmc/group__goto-programs.html), [Frama-C](https://frama-c.com/), [KLEE](https://klee-se.org/), [LAST TOOL], our Quantum Execution algorithm  

## Requirements
All the metrics provided in the paper come from experiments runned on a laptop with the following characteristics:
 - Distribution name and version: Linux Mint 21.1 (Vera)
 - Kernel version: 5.15.0-130-generic
 - RAM: 16 GB
 - Python: 3.11
 - Angr: 9.2.137
 - Frama-C: 29.0 (Copper)
 - GOTO: 6.3.1 (cbmc-6.3.1)
 - KLEE: 3.1
 - LLVM: 14.0.0
 - Clang: Ubuntu clang version 14.0.0-1ubuntu1.1; Target: x86_64-pc-linux-gnu; Thread model: posix
 - gcc: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0

The Python modules and their version used in this poject can be found at [LINK].

## Acknowledgements

We acknowledge the use of [QArithmetics](https://github.com/hkhetawat/QArithmetic). Modifications were made to adapt it for the latest version of Qiskit. We also acknowledge the use of multiple programs from the [SV-Benchmarking repository](https://gitlab.com/sosy-lab/benchmarking/sv-benchmarks/-/tree/main/c?ref_type=heads), which were modified for our purpose.

