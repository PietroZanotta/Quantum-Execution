import subprocess
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

# c_file = os.path.join(script_dir, "counting_unrolled_64.c")
# c_file = os.path.join(script_dir, "counting_unrolled_128.c")
c_file = os.path.join(script_dir, "counting_unrolled_256.c")
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
