import os
import subprocess
import re
import shutil
import random
import numpy as np
import itertools


# Set the paths and program names
file = "closest_odd"
source_file = f'{file}.c'  

def run_ikos():
    try:
        process = subprocess.run(
            ["ikos", f"{source_file}"],
            capture_output=True,
            text=True,  
            check=False 
        )
        print(process.stdout)
        return process.stdout
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def run_concrete_program(inp):
    """
    Run the program with the provided inputs (the tuple).
    """
    result = []

    for i in inp:
        i = i % 8
        
        command = [f"./{file}"]
        process = subprocess.run(command, input=f"{i}", text=True, capture_output=True)

        result.append(str(int(process.stdout.strip())))
        # print(str(i) + " -> " + str(int(process.stdout.strip())))

    if process.returncode != 0:
        print(f"Error running the concrete program: {stderr.decode()}")
        return None


    return result


def compile_program():
    try:
        subprocess.run(["gcc", source_file, "-o", file], check=True, capture_output=True, text=True)
        # print("Compilation successful")
    except subprocess.CalledProcessError as e:
        print(f"Compilation failed:\n{e.stderr}")


random.seed(1)  
n = 7
fp_list = []
fn_list = []

# Read the original content of the C file
with open(source_file, "r") as o_file:
    original_content = o_file.readlines()

# Locate the line containing the initial conditions
assert_line_index = next(
    i for i, line in enumerate(original_content) if "    // placeholder" in line
)

# Locate the line containing the assertion
line_index = next(
    i for i, line in enumerate(original_content) if "    // placeholder assert" in line
)

# Store the original assertion line
original_assert_line = original_content[assert_line_index]

# Loop through tuple lengths from 2 to 7
for tuple_length in range(2, n+1):
    # Generate all possible tuples of the current length
    tuples = list(itertools.permutations(range(n + 1), tuple_length))
    
    # Randomly select 2 tuples of the current length
    if len(tuples) < 2:
        print(f"Not enough tuples of length {tuple_length} to select.")
        # print(selected_tuples)
        continue
    
    random_float_1 = int(np.ceil(random.uniform(0, len(tuples) - 1)))
    random_float_2 = int(np.ceil(random.uniform(0, len(tuples) - 1)))
    selected_tuple_1 = tuples[random_float_1]
    selected_tuple_2 = tuples[random_float_2]

    selected_tuples = [selected_tuple_1, selected_tuple_2]

    primes = [2, 3, 5, 7, 11, 13, 17]


    for t in selected_tuples:
        concrete_output = []
        ikos_output = []

        # compile the program
        compile_program()

        # run the program
        concrete_output = run_concrete_program(t)

        # print(str(t) + "->" + str(concrete_output))

        # remove the placeholders and substitute it  
        if_else_chain = ""
        for num, p in zip(t, primes[0:len(t)]):
            if_else_chain += f"if (a % {p} == 0) {{ a = {num}; }} else "

        if_else_chain = if_else_chain[:-6]  # Remove the last else

        modified_content = original_content[:]
        modified_content[assert_line_index+1] = if_else_chain + "\n"

        with open(source_file, "w") as o_file:
            o_file.writelines(modified_content)


        # TODO: run ikos for each iteration
        run_ikos()


        # TODO: compute the fp and fn rates
        # fp_rate = len(unique_outputs-concrete_set)/len(unique_outputs) 
        # fn_rate = len(concrete_set-unique_outputs)/len(concrete_set) 
        # print("\n\n")
        # print(fp_rate)
        # print("\n\n")

        # fp_list.append(fp_rate)
        # fn_list.append(fn_rate)

        # print("\nfp: " + str(fp_rate))
        # print("fn: " + str(fn_rate) + "\n")

        # print(concrete_set)
        # print(unique_outputs)


    

        # Revert the C file to its original assertion line
        modified_content[assert_line_index] = original_assert_line
        with open(source_file, "w") as o_file:
            o_file.writelines(modified_content)

# Restore the original content of the file
with open(source_file, "w") as o_file:
    o_file.writelines(original_content)
# print(fp_list)
# average_fp = sum(fp_list) / len(fp_list)
# average_fn = sum(fn_list) / len(fn_list)

# print(f"Average FP ratio across all experiments: {average_fp}")
# print(f"Average FN ratio across all experiments: {average_fn}")
os.remove(file)
