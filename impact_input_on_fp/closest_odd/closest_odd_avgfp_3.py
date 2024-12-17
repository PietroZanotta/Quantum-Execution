import itertools
import subprocess
import time
import re
import os

n = 7

file = "closest_odd.c"

# Define the C file to modify and the terminal command
script_dir = os.path.dirname(os.path.abspath(__file__))
c_file = os.path.join(script_dir, file)
terminal_command = f"frama-c -eva -eva-unroll-recursive-calls 10 {c_file}"

# Generate all unique pairs (a, b) for a, b in range(0, 8)
tuples = list(itertools.permutations(range(n+1), 3))

# Convert each tuple to a sorted tuple to ignore order
tuples_dict = {tuple(sorted(t)) for t in tuples}

# Convert back to list if needed
pairs = list(tuples_dict)

# Read the original content of the C file
with open(c_file, "r") as o_file:
    original_content = o_file.readlines()

# Locate the line containing the assertion
assert_line_index = next(
    i for i, line in enumerate(original_content) if "assert x == a || x == b" in line
)

# Store the original assertion line
original_assert_line = original_content[assert_line_index]
fp_list=[]

# Loop through each pair, modify the file, and run the commands
for a, b, c in pairs:
    # Modify the assert line for the current pair
    modified_line = f"    /*@ assert x == {a} || x == {b} || x == {c}; */\n"
    modified_content = original_content[:]
    modified_content[assert_line_index] = modified_line

    # Write the modified content back to the file
    with open(c_file, "w") as o_file:
        o_file.writelines(modified_content)

    # Run the specified terminal command and capture output
    try:
        print(f"Running command for pair ({a}, {b}, {c}):")
        result = subprocess.run(
            terminal_command, shell=True, text=True, capture_output=True
        )
        frama_output = result.stdout
        print(f"Command Output for pair ({a}, {b}, {c}):")
        print(frama_output)
    except Exception as e:
        print(f"Error executing command for pair ({a}, {b}, {c}): {e}")
        continue

    # Adjust the regex for both formats
    closest_match = re.search(r"closest ∈ (\{[0-9; ]+\}|\[[0-9.]+\])", frama_output)

    if closest_match:
        closest_values = closest_match.group(1)
        if closest_values.startswith("{"):
            # Parse as a set of discrete values
            frama_closest = set(map(int, closest_values.strip("{}").split("; ")))
        elif closest_values.startswith("["):
            # Parse as a range
            range_bounds = list(map(int, closest_values.strip("[]").split("..")))
            frama_closest = set(range(range_bounds[0], range_bounds[1] + 1))
        # print(f"Closest values from Frama-C: {frama_closest}")
    else:
        # print("No closest values found in Frama-C output.")
        frama_closest = set()

    # print(f"Compiling file: /home/pietro/Desktop/cu/average_fp/{str(file)}, type: {type(str(file))}")



    # Run the compiled C program manually with inputs `a` and `b`
    try:
        compile_result = subprocess.run(
            ["gcc", f"{str(c_file)}", "-o", "test"], text=True, capture_output=True
        )
        if compile_result.returncode != 0:
            print("Compilation failed:")
            print(compile_result.stderr)
            exit(1)  # Exit the script if compilation fails
    except Exception as e:
        print(f"Error during compilation: {e}")
        exit(1)

    # Run the compiled program with inputs a and b
    program_results = set()
    for input_value in [a, b, c]:
        try:
            run_result = subprocess.run(
                ["./test"], input=f"{input_value}\n", text=True, capture_output=True
            )
            program_results.add(int(run_result.stdout.strip()))
        except Exception as e:
            print(f"Error running the compiled program with input {input_value}: {e}")
            continue

    # Check conditions and break if necessary
    numbers_exceed_7 = any(x > 7 for x in frama_closest | program_results)
    if numbers_exceed_7:
        print(f"Error: Some values exceed 7 in results for ({a}, {b}, {c}).")
        break

    # Output the results
    print(f"Inputs {a} and {b} and {c}")

    # Compare results
    only_in_frama = frama_closest - program_results
    overlap = frama_closest & program_results
    ratio = len(only_in_frama) / len(frama_closest) if frama_closest else 0

    print(f"Comparison: \n\tFrama-C = {frama_closest}, \n\tProgram = {program_results}")
    print(f"Overlap: {overlap}")
    print(f"Elements only in Frama-C: {only_in_frama}")
    print(f"Ratio of elements only in Frama-C to total in Frama-C: {ratio}\n")

    fp_list.append(ratio)

    # Wait 5 seconds before proceeding to the next pair
    # time.sleep(5)

    # Revert the C file to its original assertion line
    modified_content[assert_line_index] = original_assert_line
    with open(c_file, "w") as o_file:
        o_file.writelines(modified_content)

# Restore the original content of the file after all iterations
with open(c_file, "w") as o_file:
    o_file.writelines(original_content)

print("All pairs processed, and file restored.")

print(sum(fp_list)/len(fp_list))