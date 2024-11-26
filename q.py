import re

# Read the input file
with open('/home/pietro/Desktop/cu/unrolled_classical_programs/fibo_2calls_5-1.c_unrolled.c', 'r') as file:
    c_code = file.readlines()

# Regular expression to match conditions like `n-a < b` or `n-a == b`
pattern = r'if\s*\(\s*([\w\d_]+-[\w\d_]+)\s*([<==]+)\s*([\w\d_]+)\s*\)'

# List to store modified lines
modified_code = []

for line in c_code:
    # Check for matches in the line
    match = re.search(pattern, line)
    if match:
        # Extract the components of the condition
        expr, operator, b = match.groups()
        var, subtracted = expr.split('-')

        # Check if the subtracted part and `b` are numeric
        if subtracted.isdigit() and b.isdigit():
            # Perform the arithmetic
            new_value = int(subtracted) + int(b)
            # Construct the modified condition
            if operator == '<':
                modified_condition = f"if({var}-{new_value}<0)"
            elif operator == '==':
                modified_condition = f"if({var}-{new_value}==0)"
        else:
            # If not numeric, just adjust the format generically
            modified_condition = f"if({expr}-{b}{operator}0)"
        
        # Replace the old condition with the new one
        line = re.sub(pattern, modified_condition, line)
    modified_code.append(line)

# Write the modified code back to a new file
with open('output.c', 'w') as file:
    file.writelines(modified_code)

print("Simplification complete. Check 'output.c' for the updated code.")
