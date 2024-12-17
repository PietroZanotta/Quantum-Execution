'''
1. capire come runnare il comando di goto e ritrovare i valori
2. confrontare i valori con quanto ottenuto runnando normale
3. vedere di modificare i valori all'interno del file c in modo decente
4. assicurarsi che randomness sia la stessa
4. wrappare tutto con un for loop
'''
import numpy as np
import itertools
import subprocess
import random
import re
import os

random.seed(1)  
n = 7
fp_list = []
fn_list = []

file = "Et1_true.c"
c_file = f"/home/pietro/Desktop/cu/vra_methods_comparison/cbmc/{file}"
terminal_command = f"goto-analyzer --show --vsd --vsd-values intervals /home/pietro/Desktop/cu/vra_methods_comparison/cbmc/{file}"

# Read the original content of the C file
with open(c_file, "r") as o_file:
    original_content = o_file.readlines()

# Locate the line containing the assertion
assert_line_index = next(
    i for i, line in enumerate(original_content) if "  if(0==0){}" in line
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


    
    print(selected_tuples)

    primes = [2, 3, 5, 7, 11, 13, 17]
    if_else_chain = ""
    for t in selected_tuples:
        for num, p in zip(t, primes[0:len(t)]):
            if_else_chain += f"if (y % {p} == 0) {{ y = {num}; }} else "


        if_else_chain = if_else_chain[:-6]  # Remove the last else

        modified_content = original_content[:]
        modified_content[assert_line_index+1] = if_else_chain + "\n"
        print(assert_line_index)  

        with open(c_file, "w") as o_file:
            o_file.writelines(modified_content)

        # # print(modified_line)
        
        # Run the specified terminal command and capture output
        try:
            result = subprocess.run(
                terminal_command, shell=True, text=True, capture_output=True
            )

            # print(result)
            cbmc_output = result.stdout
        except Exception as e:
            # print(f"Error executing CBMC command for tuple {t}: {e}")
            continue
        
        # Get values from cbmc
        matches = re.findall(r"prefunc#return_value \(\) -> \[(\d+), (\d+)\]", cbmc_output)

        if matches:
            # Extract the last match
            a, b = map(int, matches[-1])
            # Create a set including all elements between a and b, modulo 7
            cbmc_closest = {x % 7 for x in range(a, b + 1)}
            # # print("Last range:", (a, b))
            # # print("Resulting set (modulo 7):", cbmc_closest)
        elif "prefunc#return_value () -> TOP" in cbmc_output:
            # Handle the TOP case
            cbmc_closest = {0, 1,2,3,4,5,6,7}
            print("CBMC returned TOP. Resulting set:", cbmc_closest)
        else:
            # Default case if no matches or TOP is found
            cbmc_closest = set()
            print("No valid range or TOP found in CBMC output. Output was:")
            print(cbmc_output)
            cbmc_closest = {0, 1,2,3,4,5,6,7}
        
        # print(cbmc_closest)

        def overflow_set(input_set, bit_size):
            max_value = (1 << bit_size) - 1 
            return {x & max_value for x in input_set}

        cbmc_closest = overflow_set(cbmc_closest, 3)

        # Compile and run the C program
        try:
            subprocess.run(
                ["gcc", f"/home/pietro/Desktop/cu/vra_methods_comparison/cbmc/{str(file)}", "-o", "et1"], text=True, capture_output=True
            )
        except Exception as e:
            # # print(f"Error during compilation: {e}")
            continue
        program_results = set()
        for input_value in t:
            try:
                run_result = subprocess.run(
                    ["./et1"], input=f"{input_value}\n", text=True, capture_output=True
                )
                program_results.add(int(run_result.stdout.strip()))
            except Exception as e:
                # # print(f"Error running compiled program with input {input_value}: {e}")
                continue
        # Compare results
        only_in_cbmc = cbmc_closest - program_results
        only_in_res = program_results - cbmc_closest
        
        # print(cbmc_closest)
        # print(program_results)
        print(only_in_cbmc)

        ratio = len(only_in_cbmc) / len(cbmc_closest) if cbmc_closest else 0
        # # print(ratio)
        fp_list.append(ratio)

        ratio = len(only_in_res) / len(program_results) if program_results else 0
        # # print(ratio)
        fn_list.append(ratio)

        # Revert the C file to its original assertion line
        modified_content[assert_line_index] = original_assert_line
        with open(c_file, "w") as o_file:
            o_file.writelines(modified_content)
# Restore the original content of the file

with open(c_file, "w") as o_file:
    o_file.writelines(original_content)
average_fp = sum(fp_list) / len(fp_list)
average_fn = sum(fn_list) / len(fn_list)

print(f"Average FP ratio across all experiments: {average_fp}")
print(f"Average FN ratio across all experiments: {average_fn}")