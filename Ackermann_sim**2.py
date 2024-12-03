import subprocess
import pandas as pd

# Path to the C file
c_file = "/home/pietro/Desktop/cu/classical_programs/frama-c/Ackermann01-1.c"

# Compile the C code
compile_command = ["gcc", c_file, "-o", "ackermann"]
compilation = subprocess.run(compile_command, capture_output=True, text=True)

if compilation.returncode != 0:
    print("Compilation failed!")
    print(compilation.stderr)
    exit(1)

# Run the compiled binary with all combinations of m and n
results = []
for m in range(3):
    for n in range(3):
        try:
            # Run the compiled C code
            process = subprocess.run(
                ["./ackermann"],
                input=f"{m}\n{n}\n",  # Pass m and n as input
                capture_output=True,
                text=True,
                timeout=5  # Limit execution time to avoid infinite recursion
            )
            
            # Parse the output
            output = process.stdout.strip()
            if process.returncode == 0:
                results.append((m, n, output))
            else:
                results.append((m, n, f"Error: {process.stderr.strip()}"))
        except subprocess.TimeoutExpired:
            results.append((m, n, "Timeout"))

# Print the results
for m, n, result in results:
    print(f"Ackermann({m}, {n}) = {result}")

# Save results to a list
print("Results:")

clean_results=[]
for i in range(0, len(results)):
    clean_results.append(int(results[i][2]))   

print(pd.unique(clean_results))
# print(results)
