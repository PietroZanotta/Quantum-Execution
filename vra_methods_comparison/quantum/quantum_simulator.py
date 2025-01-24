import subprocess
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

# c_file = os.path.join(script_dir, "Ackermann01-1.c")
# c_file = os.path.join(script_dir, "afterrec-1.c")
# c_file = os.path.join(script_dir, "closest_odd.c")
# c_file = os.path.join(script_dir, "closest_prime.c")
# c_file = os.path.join(script_dir, "counting.c")
# c_file = os.path.join(script_dir, "closest_odd.c")
# c_file = os.path.join(script_dir, "divbin.c")
# c_file = os.path.join(script_dir, "divbin2_unwindbound5.c")
# c_file = os.path.join(script_dir, "Et1_true.c")
# c_file = os.path.join(script_dir, "factorial.c")
# c_file = os.path.join(script_dir, "fibo_2calls_5-1.c")
# c_file = os.path.join(script_dir, "fibonacci.c")
# c_file = os.path.join(script_dir, "flow_sensitive.c")
# c_file = os.path.join(script_dir, "gcd.c")
# c_file = os.path.join(script_dir, "gcd01_2.c")
# c_file = os.path.join(script_dir, "min_num.c")
# c_file = os.path.join(script_dir, "nested_1.c")
# c_file = os.path.join(script_dir, "nested_2.c")
# c_file = os.path.join(script_dir, "num_conversion_2.c")
# c_file = os.path.join(script_dir, "num_digits_bin.c")
# c_file = os.path.join(script_dir, "parity_transform.c")
# c_file = os.path.join(script_dir, "prodbin-both-nr.c")
# c_file = os.path.join(script_dir, "sum_digits.c")

executable = os.path.join(script_dir, "myCProg")

try:
    print(f"Compiling {c_file}...")
    subprocess.run(
        ["gcc", "-o", executable, c_file], 
        check=True  
    )
    print(f"Compilation successful: {executable}")
except subprocess.CalledProcessError as e:
    print(f"Compilation failed: {e}")
    exit(1) 

input_list = [0, 1, 2, 3, 4, 5, 6]


myList = []

# simulate the quantum execution and print the result
for i in input_list:
    try:
        result = subprocess.run(
            [executable],
            input=str(i),
            text=True,
            capture_output=True,
            check=True
        )
        myList.append(int(result.stdout.strip()))  
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running the program: {e}")
        myList.append(None) 

print("Results:", myList)
