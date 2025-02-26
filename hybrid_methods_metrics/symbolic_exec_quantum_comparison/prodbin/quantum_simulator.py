# script simulating a quantum computer and running the specific c program

import subprocess
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

# c_file = os.path.join(script_dir, "prodbin-both-nr_unrolled_2.c")
c_file = os.path.join(script_dir, "prodbin-both-nr_unrolled_4.c")
# c_file = os.path.join(script_dir, "prodbin-both-nr_unrolled_8.c")
executable = os.path.join(script_dir, "myCProg")

try:
    print(f"Compiling {c_file}...")
    command = ["gcc", "-o", executable, c_file]

    print("Running command:", " ".join(command))
    subprocess.run(
        ["gcc", "-o", executable, c_file], 
        check=True  
    )
    print(f"Compilation successful: {executable}")
except subprocess.CalledProcessError as e:
    print(f"Compilation failed: {e}")
    exit(1) 

a = 0   
b = 7

myList = []

for i in range(a, b+1):
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
