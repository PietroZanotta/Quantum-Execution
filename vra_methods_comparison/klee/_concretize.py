# import re
# import os

# def convert_c_file(input_file, output_file):
#     with open(input_file, 'r') as f:
#         c_code = f.read()

#     # Remove the `#include <klee/klee.h>` line
#     c_code = re.sub(r'#include <klee/klee.h>\n', '', c_code)

#     # Replace `klee_make_symbolic(&a, sizeof(a), "a");` with `scanf("%d", &a);`
#     c_code = re.sub(r'klee_make_symbolic\(&a, sizeof\(a\), "a"\);', 'scanf("%d", &a);', c_code)

#     # Remove the `klee_warning` line entirely
#     c_code = re.sub(r'klee_warning\((.*)\);', '', c_code)

#     # Add printf instead of klee_warning
#     c_code = re.sub(r'snprintf\((.*), (.*), "(.*)", (.*)\);', r'printf("%s", \3);', c_code)

#     # Write the modified code to the output file
#     with open(output_file, 'w') as f:
#         f.write(c_code)

#     print(f"Conversion complete. The modified code has been saved to {output_file}")

# def process_all_c_files():
#     # Get the current working directory
#     current_directory = os.getcwd()

#     # Loop through all files in the directory
#     for filename in os.listdir(current_directory):
#         # Check if the file is a .c file
#         if filename.endswith('.c'):
#             input_file = filename
#             output_file = f"{filename[:-2]}_concrete.c"  # Create output file name by appending '_concrete'

#             # Call the function to convert the C file
#             convert_c_file(input_file, output_file)

# # Run the function to process all C files in the current directory
# process_all_c_files()


import re

def convert_c_file(input_file, output_file):
    with open(input_file, 'r') as f:
        c_code = f.read()

    # Remove the `#include <klee/klee.h>` line
    c_code = re.sub(r'#include <klee/klee.h>\n', '', c_code)

    # Replace `klee_make_symbolic(&a, sizeof(a), "a");` with `scanf("%d", &a);`
    c_code = re.sub(r'klee_make_symbolic\(&a, sizeof\(a\), "a"\);', 'scanf("%d", &a);', c_code)

    # Remove the `klee_warning` line entirely
    c_code = re.sub(r'klee_warning\((.*)\);', '', c_code)

    # Add printf instead of klee_warning
    c_code = re.sub(r'// placeholder', r'   printf("%d", result);', c_code)

    # Write the modified code to the output file
    with open(output_file, 'w') as f:
        f.write(c_code)

    print(f"Conversion complete. The modified code has been saved to {output_file}")

# file = "afterrec-1"
# input_file = f'{file}.c'  
# output_file = f'{file}_concrete.c' 

# convert_c_file(input_file, output_file)



def convert_c_file_2_inputs(input_file, output_file):
    with open(input_file, 'r') as f:
        c_code = f.read()

    # Remove the `#include <klee/klee.h>` line
    c_code = re.sub(r'#include <klee/klee.h>\n', '', c_code)

    # Replace `klee_make_symbolic(&a, sizeof(a), "a");` with `scanf("%d", &a);`
    c_code = re.sub(r'klee_make_symbolic\(&a, sizeof\(a\), "a"\);', 'scanf("%d", &a);', c_code)

    # Replace `klee_make_symbolic(&b, sizeof(b), "b");` with `scanf("%d", &b);`
    c_code = re.sub(r'klee_make_symbolic\(&b, sizeof\(b\), "b"\);', 'scanf("%d", &b);', c_code)

    # Remove the `klee_warning` line entirely
    c_code = re.sub(r'klee_warning\((.*)\);', '', c_code)

    # Add printf instead of klee_warning
    c_code = re.sub(r'// placeholder', r'   printf("%d", result);', c_code)

    # Write the modified code to the output file
    with open(output_file, 'w') as f:
        f.write(c_code)

    print(f"Conversion complete. The modified code has been saved to {output_file}")




def convert_c_file_3_inputs(input_file, output_file):
    with open(input_file, 'r') as f:
        c_code = f.read()

    # Remove the `#include <klee/klee.h>` line
    c_code = re.sub(r'#include <klee/klee.h>\n', '', c_code)

    # Replace `klee_make_symbolic(&a, sizeof(a), "a");` with `scanf("%d", &a);`
    c_code = re.sub(r'klee_make_symbolic\(&a, sizeof\(a\), "a"\);', 'scanf("%d", &a);', c_code)

    # Replace `klee_make_symbolic(&b, sizeof(b), "b");` with `scanf("%d", &b);`
    c_code = re.sub(r'klee_make_symbolic\(&b, sizeof\(b\), "b"\);', 'scanf("%d", &b);', c_code)

    # Replace `klee_make_symbolic(&c, sizeof(c), "c");` with `scanf("%d", &c);`
    c_code = re.sub(r'klee_make_symbolic\(&c, sizeof\(c\), "c"\);', 'scanf("%d", &c);', c_code)

    # Remove the `klee_warning` line entirely
    c_code = re.sub(r'klee_warning\((.*)\);', '', c_code)

    # Add printf instead of klee_warning
    c_code = re.sub(r'// placeholder', r'   printf("%d", result);', c_code)

    # Write the modified code to the output file
    with open(output_file, 'w') as f:
        f.write(c_code)

    print(f"Conversion complete. The modified code has been saved to {output_file}")