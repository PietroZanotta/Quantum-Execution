# quantum simulator running the c programs below

import subprocess
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

# c_file = os.path.join(script_dir, "closest_odd.c")
# c_file = os.path.join(script_dir, "flow_sensitive.c")
# c_file = os.path.join(script_dir, "fibo_2calls_5-1.c")
# c_file = os.path.join(script_dir, "afterrec-1.c")
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

myList = []

for i in range(a, b):
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
