import angr
import claripy
import itertools
import logging
import random
import numpy as np

random.seed(1)

# Load the binary
proj = angr.Project("./factorial", auto_load_libs=False)
func = "factorial"

logging.getLogger("angr").setLevel(logging.ERROR)
logging.getLogger("cle").setLevel(logging.ERROR)
logging.getLogger("pyvex").setLevel(logging.ERROR)
logging.getLogger("claripy").setLevel(logging.ERROR)


# Define the symbolic variable x
x = claripy.BVS("x", 32)

# The range of numbers
n = 7
numbers = list(range(n + 1))

fp = []
fn = []

# Loop through tuple lengths from 2 to 7
for tuple_length in range(2, n+1):
    # Generate all possible tuples of the current length
    all_tuples = list(itertools.combinations(numbers, tuple_length))

    # Randomly select two tuples (or pick the first two if needed)
    if len(all_tuples) < 2:
        print(f"Not enough tuples for length {tuple_length}")
        continue
    
    random_float_1 = int(np.ceil(random.uniform(0, len(all_tuples) - 1)))
    random_float_2 = int(np.ceil(random.uniform(0, len(all_tuples) - 1)))
    selected_tuple_1 = all_tuples[random_float_1]
    selected_tuple_2 = all_tuples[random_float_2]

    selected_tuples = [selected_tuple_1, selected_tuple_2]

    # Process each selected tuple
    for number_tuple in selected_tuples:
        symbolic_y_results = set()

        # Add symbolic constraint for the current tuple
        constraint = claripy.Or(*(x == num for num in number_tuple))
        initial_state = proj.factory.call_state(proj.loader.find_symbol(func).rebased_addr, x)
        initial_state.solver.add(constraint)

        # Run symbolic execution
        simgr = proj.factory.simgr(initial_state)
        simgr.run()

        for state in simgr.deadended:
            y_values = state.solver.eval_upto(state.regs.eax, 10, cast_to=int)
            symbolic_y_results.update(y_values)
        

        # Supply each value of the tuple to the binary and save the result
        concrete_y_results = set()
        for value in number_tuple:
            initial_state = proj.factory.call_state(proj.loader.find_symbol(func).rebased_addr, value)
            simgr = proj.factory.simgr(initial_state)
            simgr.run()

            for state in simgr.deadended:
                concrete_y = state.solver.eval(state.regs.eax, cast_to=int)
                concrete_y_results.add(concrete_y)
        if len(symbolic_y_results) == 0:
            print("ERROR")
        print(f"results for tuple {number_tuple}: {symbolic_y_results - concrete_y_results}")
        
        fp_rate = len(symbolic_y_results-concrete_y_results)/len(symbolic_y_results)
        fp.append(fp_rate)

        fn_rate = len(concrete_y_results-symbolic_y_results)/len(concrete_y_results)
        fn.append(fn_rate)

print(f"avg fp rate: {np.sum(fp)/len(fp)}\n")
print(f"avg fn rate: {np.sum(fn)/len(fn)}\n")
