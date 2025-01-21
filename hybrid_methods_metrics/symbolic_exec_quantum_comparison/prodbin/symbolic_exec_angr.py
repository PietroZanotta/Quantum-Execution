import angr
import claripy
import logging
import random
import numpy as np

# Load the binary
proj = angr.Project("./symbolic_exec_quantum_comparison/prodbin/myCProg", auto_load_libs=False)
func = "f"

logging.getLogger("angr").setLevel(logging.ERROR)
logging.getLogger("cle").setLevel(logging.ERROR)
logging.getLogger("pyvex").setLevel(logging.ERROR)
logging.getLogger("claripy").setLevel(logging.ERROR)

# Define the symbolic variable x
x = claripy.BVS("x", 32)

manual_list = [0, 1, 2, 3, 4, 5]

# Add symbolic constraint for the provided list
constraint = claripy.Or(*(x == num for num in manual_list))

# Initialize symbolic execution
initial_state = proj.factory.call_state(proj.loader.find_symbol(func).rebased_addr, x)
initial_state.solver.add(constraint)

# Run symbolic execution
simgr = proj.factory.simgr(initial_state)
simgr.run()

# Collect symbolic results
symbolic_y_results = set()
for state in simgr.deadended:
    y_values = state.solver.eval_upto(state.regs.eax, 10, cast_to=int)
    symbolic_y_results.update(y_values)

# Supply each value in the list to the binary and collect concrete results
concrete_y_results = set()
for value in manual_list:
    initial_state = proj.factory.call_state(proj.loader.find_symbol(func).rebased_addr, value)
    simgr = proj.factory.simgr(initial_state)
    simgr.run()

    for state in simgr.deadended:
        concrete_y = state.solver.eval(state.regs.eax, cast_to=int)
        concrete_y_results.add(concrete_y)

print(symbolic_y_results)

