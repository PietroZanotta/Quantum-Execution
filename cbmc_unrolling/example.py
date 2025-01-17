import subprocess
import re

def check_cbmc(c_file, unwind_value):
    """Runs CBMC with a given unwind value and checks for failures."""
    try:
        command = ["cbmc", c_file, f"-unwindset", f"main.0:{unwind_value}"]
        process = subprocess.run(command, capture_output=True, text=True, check=False)  # Capture output, don't raise on non-zero exit
        output = process.stdout

        if "FAILURE" in output:
            return True  # Failure found
        else:
            return False # No failure found
    except FileNotFoundError:
        print("Error: CBMC not found. Please ensure it's installed and in your PATH.")
        exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        exit(1)


def find_minimal_unwind(c_file):
    """Finds the minimal unwind value that doesn't produce failures."""
    for a in range(1, 101):
        print(f"Testing unwind value: {a}")
        if not check_cbmc(c_file, a):
            print(f"Minimal unwind value found: {a}")
            return a
    print("No suitable unwind value found within the range 1-100.")
    return None

if __name__ == "__main__":
    c_file = "example.c"  # Replace with your C file name

    # Check if the C file exists
    try:
        with open(c_file, 'r'):
            pass
    except FileNotFoundError:
        print(f"Error: C file '{c_file}' not found.")
        exit(1)

    minimal_a = find_minimal_unwind(c_file)

    if minimal_a:
        print(f"To run CBMC with the minimal unwind value: cbmc {c_file} -unwindset main.0:{minimal_a}")