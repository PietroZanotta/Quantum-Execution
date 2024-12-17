import subprocess
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

# c_file = os.path.join(script_dir, "Ackermann01-1.c")
# c_file = os.path.join(script_dir, "closest_prime.c")
# c_file = os.path.join(script_dir, "closest_prime.c")
# c_file = os.path.join(script_dir, "Et1_true.c")
# c_file = os.path.join(script_dir, "factorial.c")
# c_file = os.path.join(script_dir, "fibonacci.c")
# c_file = os.path.join(script_dir, "gcd.c")
# c_file = os.path.join(script_dir, "min_num.c")
# c_file = os.path.join(script_dir, "nested_1.c")
# c_file = os.path.join(script_dir, "nested_2.c")
# c_file = os.path.join(script_dir, "num_digits_bin.c")
# # # c_file = os.path.join(script_dir, "prodbin-both-nr.c")
# # # c_file = os.path.join(script_dir, "reverse_number_digits.c")
# c_file = os.path.join(script_dir, "sum_digits.c")
# c_file = os.path.join(script_dir, "68-longjmp_04-counting-local_unknown_1_neg.c")
# c_file = os.path.join(script_dir, "afterrec-1.c")
# c_file = os.path.join(script_dir, "fibo_2calls_5-1.c")
c_file = os.path.join(script_dir, "flow_sensitive.c")
# c_file = os.path.join(script_dir, ".c")
# c_file = os.path.join(script_dir, ".c")
# c_file = os.path.join(script_dir, ".c")
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

a = 0
b = 8
c = 0
d = 8

myList = []

for j in range(a, b):
    for i in range(c, d):
        try:
            result = subprocess.run(
                [executable],
                # input=str(j), 
                input=f"{j}\n{i}\n", 
                text=True,
                capture_output=True,
                check=True
            )
            if result.stdout.strip() != "":
                myList.append(int(result.stdout.strip()))
                print(f"i: {i} j: {j} -> {int(result.stdout.strip())}")
            
            # print(f"gcd({i}, {j}) = {int(result.stdout.strip())}")
        
        except subprocess.CalledProcessError as e:
            print(f"Error occurred while running the program: {e}")
            myList.append(None) 

import pandas

print("Results:", pandas.unique(myList))
