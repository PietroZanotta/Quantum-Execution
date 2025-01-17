import os
import subprocess
import re

def extract_ktest_values(ktest_file):
    """Extracts uint values from a .ktest file."""
    command = f"ktest-tool {ktest_file}"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if process.returncode != 0:
        print(f"Error extracting values from {ktest_file}: {stderr.decode()}")
        return None

    ktest_data = stdout.decode().strip()
    pattern = r"object \d+: uint:\s*(\d+)"
    matches = re.findall(pattern, ktest_data)
    uint_values = [int(match) for match in matches]
    return uint_values

def get_all_uint_values_from_dir(klee_out_dir):
    """Retrieves all uint values from all .ktest files in a directory."""
    all_uint_values = []
    ktest_files = [f for f in os.listdir(klee_out_dir) if f.endswith('.ktest')]

    if not ktest_files:
        print(f"No .ktest files found in {klee_out_dir}")
        return []

    for ktest_file in ktest_files:
        ktest_path = os.path.join(klee_out_dir, ktest_file)
        uint_values = extract_ktest_values(ktest_path)
        if uint_values:  # Check if uint_values is not None
            all_uint_values.extend(uint_values)
    return all_uint_values

# Example usage:

all_div_8 = []
for i in range(0, 12):
    klee_output_directory = f"klee-out-{i}"  # Replace with your KLEE output directory
    all_values = get_all_uint_values_from_dir(klee_output_directory)

    if all_values:
        print(f"All extracted uint values from {klee_output_directory}: {all_values}")
    else:
        print(f"No uint values extracted from {klee_output_directory}")

    for i in all_values:
        all_div_8.append(i%8)

print(set(all_div_8))

# credo il problema stia nel %8
# controlla che anche gli altri loop siano scartate 10 volte