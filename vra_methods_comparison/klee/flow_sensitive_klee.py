import os
import subprocess
import re
import shutil
import random
import numpy as np
from _concretize import convert_c_file_2_inputs
import itertools


# Set the paths and program names
file = "flow_sensitive"
# file = "test"
source_file = f'{file}.c'  # Replace with your source file
program_name = f'{file}.bc'  # Name of the compiled program (after `clang` compilation)
file_concrete_source = f'{file}_concrete.c'  # C file that contains the concrete program
file_concrete_program = f'{file}_concrete'  # The compiled executable for test_concrete
klee_out_dir = 'klee-out-0'  # KLEE output directory
klee_last_dir = 'klee-last'  # KLEE output directory

# Function to compile the source code to LLVM bitcode
def compile_to_bitcode(source_file):
    # Compile the C code to LLVM bitcode
    command = f'clang -emit-llvm -c -g {source_file} -o {file}.bc -I/home/linuxbrew/.linuxbrew/include'
    print(f"Running command: {command}")
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    
    if process.returncode != 0:
        print(f"Error during compilation: {stderr.decode()}")
        return False
    print(f"Compilation successful. Bitcode saved to {file}.bc")
    return True

# Function to compile the concrete C program
def compile_concrete_program():
    # Compile the concrete C program to create the executable
    command = f'gcc {file_concrete_source} -o {file_concrete_program}'
    print(f"Running command: {command}")
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    
    if process.returncode != 0:
        print(f"Error during concrete program compilation: {stderr.decode()}")
        return False
    print(f"Concrete program compiled successfully: {file_concrete_program}")
    return True

# Function to run KLEE and generate the test cases
def run_klee():
    # Run KLEE on the bitcode file to generate the test cases
    command = f'klee {file}.bc'
    print(f"Running command: {command}")
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    
    if process.returncode != 0:
        print(f"Error during KLEE execution: {stderr.decode()}")
        return False
    print(f"KLEE executed successfully. Test cases generated in {klee_out_dir}")
    return True

# Function to extract concrete uint values from the KLEE-generated .ktest file
def extract_ktest_values(ktest_file):
    """
    Extracts concrete input values from a KLEE test case (.ktest) file.
    The KLEE test case is assumed to be a plain string with input data.
    """
    command = f"ktest-tool {ktest_file}"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if process.returncode != 0:
        print(f"Error extracting values from {ktest_file}: {stderr.decode()}")
        return None

    # Parse the stdout to extract the uint values using regex
    ktest_data = stdout.decode().strip()
    
    # Regex to match the 'uint' value (e.g., "uint: 2147483648")
    pattern = r"object \d+: uint:\s*(\d+)"
    matches = re.findall(pattern, ktest_data)

    # Convert the matches to integers
    uint_values = [int(match) for match in matches]
    # print(uint_values)

    return uint_values

# Function to run the concrete program with the extracted input values
def run_concrete_program(inp):
    """
    Run the concrete program with the provided inputs.
    """
    inp = inp[0] % 8

    # Prepare the command to run the program with the concrete inputs
    # We will pass the inputs as command-line arguments to the program
    # print(inp)
    command = [f"./{file_concrete_program}"]
    
    # ["gcc", f"/home/pietro/Desktop/cu/vra_methods_comparison/frama-c/{str(file)}", "-o", "gcd"]

    process = subprocess.run(command, input=f"{inp}", text=True, capture_output=True)
    # stdout, stderr = process.communicate()
    if process.returncode != 0:
        print(f"Error running the concrete program: {stderr.decode()}")
        return None

    print(str(inp) + " -> " + str(int(process.stdout.strip())))

    return int(process.stdout.strip())%8
    # return stdout.decode().strip()

# Function to print the unique outputs
def print_unique_outputs(unique_outputs):
    print("\nUnique Outputs:")
    print("\n")
    for output in unique_outputs:
        print(output)
    print("\n")

# Cleanup function to remove generated directories and files
def cleanup():
    # Remove KLEE output directory if it exists
    if os.path.exists(klee_out_dir):
        print(f"Cleaning up KLEE output directory: {klee_out_dir}")
        shutil.rmtree(klee_out_dir)

    if os.path.exists(klee_last_dir):
        print(f"Cleaning up KLEE output directory: {klee_last_dir}")
        shutil.rmtree(klee_last_dir)

    # Remove the compiled concrete program if it exists
    if os.path.exists(file_concrete_program):
        print(f"Cleaning up concrete program: {file_concrete_program}")
        os.remove(file_concrete_program)

    # Remove the compiled bitcode if it exists
    if os.path.exists(f'{file}.bc'):
        print(f"Cleaning up bitcode file: {file}.bc")
        os.remove(f'{file}.bc')
    



def concrete_execution():
    unique_concrete = set()

    for inp in range(8):
        command = [f"./{file_concrete_program}"]
        process = subprocess.run(command, input=f"{inp}", text=True, capture_output=True)
        res = int(process.stdout.strip())%8
        unique_concrete.add(res)
    
    return unique_concrete


random.seed(1)  
n = 7
fp_list = []
fn_list = []

# Read the original content of the C file
with open(source_file, "r") as o_file:
    original_content = o_file.readlines()

# Locate the line containing the assertion
assert_line_index = next(
    i for i, line in enumerate(original_content) if "  if(0==0){}" in line
)

# Create concrete execution file
convert_c_file_2_inputs(source_file, file_concrete_source)

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
    if_else_chain = ""
    
    for t in selected_tuples:
        for num, p in zip(t, primes[0:len(t)]):
            if_else_chain += f"if (a % {p} == 0) {{ a = {num}; }} else "


        if_else_chain = if_else_chain[:-6]  # Remove the last else

        modified_content = original_content[:]
        modified_content[assert_line_index+1] = if_else_chain + "\n"
        print(assert_line_index)  

        with open(source_file, "w") as o_file:
            o_file.writelines(modified_content)



        try:
            # Step 1: Compile the source code to LLVM bitcode
            if not compile_to_bitcode(source_file):
                break

            # Step 2: Compile the concrete C program
            if not compile_concrete_program():
                break

            # Step 3: Run KLEE to generate the test cases
            if not run_klee():
                break

            # Step 4: Run the test cases and collect unique outputs
            unique_outputs = set()

            # List all .ktest files in the KLEE output directory
            ktest_files = [f for f in os.listdir(klee_out_dir) if f.endswith('.ktest')]

            for ktest_file in ktest_files:
                ktest_path = os.path.join(klee_out_dir, ktest_file)

                # Extract the uint values from the .ktest file
                uint_values = extract_ktest_values(ktest_path)
                if uint_values is None:
                    continue
                
                # print("int val:" + str([uint_values]) + str(type(uint_values)))
                # Run the concrete program with the extracted uint values
                for i in [uint_values]:
                    output = run_concrete_program(i)
                    # print(f"Output for {ktest_file}: {output}")
                    unique_outputs.add(output)

            concrete_set = concrete_execution()

            fp_rate = len(unique_outputs-concrete_set)/len(unique_outputs) 
            fn_rate = len(concrete_set-unique_outputs)/len(concrete_set) 
            print("\n\n")
            print(fp_rate)
            print("\n\n")

            fp_list.append(fp_rate)
            fn_list.append(fn_rate)

            print("\nfp: " + str(fp_rate))
            print("fn: " + str(fn_rate) + "\n")

            print(concrete_set)
            print(unique_outputs)

            # Step 5: Print the unique outputs
            # print_unique_outputs(unique_outputs)

        finally:
            # Cleanup generated files and directories at the end
            cleanup()

        # Revert the C file to its original assertion line
        modified_content[assert_line_index] = original_assert_line
        with open(source_file, "w") as o_file:
            o_file.writelines(modified_content)
# Restore the original content of the file

with open(source_file, "w") as o_file:
    o_file.writelines(original_content)
print(fp_list)
average_fp = sum(fp_list) / len(fp_list)
average_fn = sum(fn_list) / len(fn_list)

print(f"Average FP ratio across all experiments: {average_fp}")
print(f"Average FN ratio across all experiments: {average_fn}")
os.remove(f"{file_concrete_program}.c")
