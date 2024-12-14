import re
import subprocess
import random

# Example input: Replace this with your actual cbmc_output
cbmc_output = """
prefunc#return_value () -> [1, 10]
prefunc#return_value () -> [3, 8]
prefunc#return_value () -> [5, 15]
"""

# Find the last occurrence of the pattern
matches = re.findall(r"prefunc#return_value \(\) -> \[(\d+), (\d+)\]", cbmc_output)
if matches:
    # Extract the last match
    a, b = map(int, matches[-1])
    # Create a set including all elements between a and b, modulo 7
    result_set = {x % 7 for x in range(a, b + 1)}
else:
    result_set = set()

print("Last range:", (a, b) if matches else "None found")
print("Resulting set (modulo 7):", result_set)

# Generate C code with a specified tuple_length
def generate_c_code(tuple_length):
    c_code = []
    for i in range(1, tuple_length + 1):
        if_branch = f"if (y % x{i}) {{ return x{i}; }}"
        c_code.append(if_branch if i == 1 else f"else {if_branch}")
    c_code.append("else { return x_tuple_length; }")
    return "\n".join(c_code)

# Example usage:
tuple_length = 5
c_code_output = generate_c_code(tuple_length)
print("\nGenerated C code:")
print(c_code_output)

# Replace placeholder `if(0==0){}` with generated C code
def replace_placeholder(file_content, c_code_output):
    indented_code = "\n".join(f"    {line}" for line in c_code_output.splitlines())
    return re.sub(r"if\(0==0\)\{\}", indented_code, file_content)

# Example replacement usage
file_content = """
if(0==0){}
"""
file_content = replace_placeholder(file_content, c_code_output)
print("\nUpdated file content:")
print(file_content)

# Compile and run the C program
try:
    subprocess.run([
        "gcc", "/home/pietro/Desktop/cu/classical_programs/cbmc/Et1_true.c", "-o", "et1"
    ], check=True)
    print("Compilation successful.")
except subprocess.CalledProcessError as e:
    print(f"Compilation error: {e}")

# Example program execution
program_results = set()
for input_value in [1, 2, 3, 4, 5]:  # Replace with dynamic tuple values
    try:
        run_result = subprocess.run(
            ["./et1"], input=f"{input_value}\n", text=True, capture_output=True, check=True
        )
        program_results.add(int(run_result.stdout.strip()))
    except subprocess.CalledProcessError as e:
        print(f"Execution error for input {input_value}: {e}")

print("Program results:", program_results)

# Compare CBMC and program outputs
only_in_cbmc = result_set - program_results
ratio = len(only_in_cbmc) / len(result_set) if result_set else 0
print("FP ratio:", ratio)