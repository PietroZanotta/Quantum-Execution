import angr
import claripy
proj = angr.Project("./angr_testcase", auto_load_libs=False)
x = claripy.BVS("x", 32)
initial_state = proj.factory.call_state(proj.loader.find_symbol("symbolic").rebased_addr, x)
initial_state.solver.add(x >= 0)
initial_state.solver.add(x <= 7)
simgr = proj.factory.simgr(initial_state)
simgr.run()
possible_y_values = set()
for state in simgr.deadended:
    y_values = state.solver.eval_upto(state.regs.eax, 100, cast_to=int)
    possible_y_values.update(y_values)
print("y possible value:", possible_y_values)