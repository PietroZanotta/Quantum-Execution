import itertools
import subprocess
import random
import re
import os

random.seed(1)

n = 7
fp_list = []

file = "nested_2.c"
c_file = f"/home/pietro/Desktop/cu/classical_programs/frama-c/{file}"
terminal_command = f"frama-c -eva /home/pietro/Desktop/cu/classical_programs/frama-c/{file}"

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
                    print("Range includes 2147483647. Setting FP rate to 1.")
                    fp_list.append(1)
                    mask = 1
                    break

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
                print(frama_closest)

                # Compile and run the C program
                try:
                    subprocess.run(
                        ["gcc", f"/home/pietro/Desktop/cu/average_fp/{str(file)}", "-o", "test"], text=True, capture_output=True
                    )
                except Exception as e:
                    print(f"Error during compilation: {e}")
                    continue

                program_results = set()
                for input_value in number_t + y_t:  # Combine inputs from both tuples
                    try:
                        run_result = subprocess.run(
                            ["./test"], input=f"{input_value}\n", text=True, capture_output=True
                        )
                        program_results.add(int(run_result.stdout.strip()))
                    except Exception as e:
                        print(f"Error running compiled program with input {input_value}: {e}")
                        continue

                # Compare results
                only_in_frama = frama_closest - program_results
                ratio = len(only_in_frama) / len(frama_closest) if frama_closest else 0
                fp_list.append(ratio)

            # Revert the C file to its original assertion line
            modified_content[assert_line_index] = original_assert_line
            with open(c_file, "w") as o_file:
                o_file.writelines(modified_content)

# Restore the original content of the file
with open(c_file, "w") as o_file:
    o_file.writelines(original_content)

average_fp = sum(fp_list) / len(fp_list) if fp_list else 0
print(f"Average FP ratio across all experiments: {average_fp}")
