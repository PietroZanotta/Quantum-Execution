import angr
import claripy

# Load the binary
project = angr.Project('./gcd', auto_load_libs=False)

# Define symbolic variables
a = claripy.BVS('a', 3)
b = claripy.BVS('b', 3)

# Set up the initial state with a symbolic `stdin`
state = project.factory.entry_state(stdin=claripy.Concat(a, claripy.BVV(b, 3))) 

# Create a simulation manager
simgr = project.factory.simulation_manager(state)

# Explore all possible paths to reach the end of the program
simgr.explore()

# Collect the possible values of 'result' by inspecting the final states
result_values = set()
for final_state in simgr.deadended:
    if final_state.solver.eval_upto(a, 10) and final_state.solver.eval_upto(b, 10):  # Limit evaluations
        result = final_state.solver.eval_upto(final_state.regs.eax, 10)  # Adjust as needed
        result_values.update(result)

print(f"Possible values of 'result': {result_values}")
