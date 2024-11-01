import angr, claripy
# Load the binary
project = angr.Project('./a', auto_load_libs=False)

# Define the address of the firstCall function
firstCall_addr = project.loader.main_object.get_symbol("main")

# Define the address of the helloWorld function
helloWorld_addr = project.loader.main_object.get_symbol("signal")

# Create a symbolic variable for the firstCall arg
input_arg_a = claripy.BVS('a', 3)
input_arg_b = claripy.BVS('b', 3)

# Create a blank state at the address of the firstCall function
init_state = project.factory.blank_state(addr=firstCall_addr.rebased_addr)

# Assuming the calling convention passes the argument in a register
# (e.g., x86 uses edi for the argument)
init_state.regs.edi = input_arg_a

# Create a simulation manager
simgr = project.factory.simulation_manager(init_state)

# Explore the binary, looking for the address of helloWorld
simgr.explore(find=helloWorld_addr.rebased_addr)

# Check if we found a state that reached the target
if simgr.found:
    input_value = simgr.found[0].solver.eval(input_arg_a)
    print(f"Value of input_arg_a that reaches HelloWorld: {input_value}")
    # Get the constraints for reaching the helloWorld function
    constraints = simgr.found[0].solver.constraints
    # Create a solver with the constraints
    solver = claripy.Solver()
    solver.add(constraints)
    min_val = solver.min(input_arg_a)
    max_val = solver.max(input_arg_a)
    print(f"Function arg: min = {min_val}, max = {max_val}")
else:
    print("Did not find a state that reaches HelloWorld.")
