import itertools
import subprocess
import random
import re
import os

random.seed(1)

n = 7
fp_list = []
fn_list = []

file = "nested_2.c"
c_file = f"/home/pietro/Desktop/cu/vra_methods_comparison/frama-c/{file}"
terminal_command = f"frama-c -eva /home/pietro/Desktop/cu/vra_methods_comparison/frama-c/{file}"

# Read the original content of the C file
with open(c_file, "r") as o_file:
    original_content = o_file.readlines()

# Locate the line containing the assertion
assert_line_index = next(
    i for i, line in enumerate(original_content) if "assert h == a || h == b" in line
)

# Store the original assertion line
original_assert_line = original_content[assert_line_index]

# Loop through tuple lengths from 2 to 7
for tuple_length in range(2, 8):
    # Generate all possible tuples of the current length for `number` and `y`
    number_tuples = list(itertools.permutations(range(n + 1), tuple_length))
    y_tuples = list(itertools.permutations(range(n + 1), tuple_length))

    # Randomly select 2 tuples for `number` and `y` of the current length
    if len(number_tuples) >= 2 and len(y_tuples) >= 2:
        selected_number_tuples = random.sample(number_tuples, 2)
        selected_y_tuples = random.sample(y_tuples, 2)
    else:
        print(f"Not enough tuples of length {tuple_length} to select.")
        continue

    print(f"Selected number tuples: {selected_number_tuples}")
    print(f"Selected y tuples: {selected_y_tuples}")

    for number_t in selected_number_tuples:
        for y_t in selected_y_tuples:
            # Construct the assertion line with the current tuples for `number` and `y`
            number_condition = " || ".join([f"h == {x}" for x in number_t])
            y_condition = " || ".join([f"l == {x}" for x in y_t])
            modified_line = f"    /*@ assert ({number_condition}) && ({y_condition}); */\n"
            modified_content = original_content[:]
            modified_content[assert_line_index] = modified_line

            # Write the modified content back to the file
            with open(c_file, "w") as o_file:
                o_file.writelines(modified_content)

            # Run the specified terminal command and capture output
            try:
                result = subprocess.run(
                    terminal_command, shell=True, text=True, capture_output=True
                )
                frama_output = result.stdout
            except Exception as e:
                print(f"Error executing Frama-C command for tuple {number_t} and {y_t}: {e}")
                continue

            mask = 0

            # Check if the range includes 2147483647
            for line in frama_output.splitlines():
                # if "min" in line:
                #     print(line)
                if ("2147483646" in line or "2147483647" in line) and "min ∈" in line:
                    print("Range includes 2147483647.")
                    frama_closest = set()
                    for i in range(8):
                        frama_closest.add(i)
                    mask = 1

            if mask == 0:  # Extract closest values from Frama-C output
                closest_match = re.search(r"min ∈ (\{[0-9; ]+\}|\[[0-9.]+\])", frama_output)
                if closest_match:
                    closest_values = closest_match.group(1)
                    if closest_values.startswith("{"):
                        frama_closest = set(map(int, closest_values.strip("{}").split("; ")))
                    elif closest_values.startswith("["):
                        range_bounds = list(map(int, closest_values.strip("[]").split("..")))
                        frama_closest = set(range(range_bounds[0], range_bounds[1] + 1))
                else:
                    frama_closest = set()
                # print(frama_closest)

                def overflow_set(input_set, bit_size):
                    max_value = (1 << bit_size) - 1 
                    return {x & max_value for x in input_set}

                frama_closest = overflow_set(frama_closest, 3)


                # Compile and run the C program
            try:
                subprocess.run(
                    ["gcc", f"/home/pietro/Desktop/cu/vra_methods_comparison/frama-c/{str(file)}", "-o", "n2"], text=True, capture_output=True
                )
            except Exception as e:
                print(f"Error during compilation: {e}")
                continue

            program_results = set()
            for input_value in number_t:
                for input_value2 in y_t:
                    try:
                        run_result = subprocess.run(
                            ["./n2"], input=f"{input_value}\n{input_value2}\n", text=True, capture_output=True
                        )
                        print(str(input_value) + "  " + str(input_value2) + " -> " + str(int(run_result.stdout.strip())))
                        program_results.add(int(run_result.stdout.strip()))
                
                    except Exception as e:
                        print(f"Error running compiled program with input {input_value}: {e}")
                        continue

            # Compare results
            only_in_frama = frama_closest - program_results
            ratio = len(only_in_frama) / len(frama_closest) if frama_closest else 0
            fp_list.append(ratio)

            # fn
            only_in_manual = program_results - frama_closest
            ratio_fn = len(only_in_manual) / len(program_results) if program_results else 0
            fn_list.append(ratio_fn)


                # Revert the C file to its original assertion line
            modified_content[assert_line_index] = original_assert_line
            with open(c_file, "w") as o_file:
                o_file.writelines(modified_content)
# Restore the original content of the file
with open(c_file, "w") as o_file:
    o_file.writelines(original_content)
average_fp = sum(fp_list) / len(fp_list) if fp_list else 0
average_fn = sum(fn_list) / len(fn_list) if fn_list else 0
print(f"Average FP ratio across all experiments: {average_fp}")
print(f"Average FN ratio across all experiments: {average_fn}")