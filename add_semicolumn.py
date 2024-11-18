def add_semicolon_to_file(input_file, output_file):
    try:
        with open(input_file, 'r') as infile:
            lines = infile.readlines()

        with open(output_file, 'w') as outfile:
            for line in lines:
                stripped_line = line.strip()
                
                # Skip empty lines or comments
                if not stripped_line or stripped_line.startswith("//") or stripped_line.startswith("/*"):
                    outfile.write(line)
                    continue

                # Check if the line already ends with a semicolon
                if not stripped_line.endswith(';'):
                    # Add semicolon if missing
                    outfile.write(line.rstrip() + ';\n')
                else:
                    # Keep the line as it is
                    outfile.write(line)

        print(f"File processed successfully. Output saved to {output_file}.")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
input_filename = "/home/pietro/Desktop/cu/unrolled_classical_programs/fibo_2calls_5-1.c_unrolled.c"
output_filename = "fibo_2calls_5-1.c_unrolled_modified.c"
add_semicolon_to_file(input_filename, output_filename)
