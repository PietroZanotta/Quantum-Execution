import os
import re
import csv

def count_code_lines(filepath):
    """Count lines of code in a file, excluding blank lines and comments."""
    code_lines = 0
    in_multiline_comment = False

    with open(filepath, 'r') as file:
        for line in file:
            stripped_line = line.strip()

            # Check for multiline comments
            if '/*' in stripped_line:
                in_multiline_comment = True
            if '*/' in stripped_line:
                in_multiline_comment = False
                continue

            # Skip lines that are part of multiline comments or single-line comments
            if in_multiline_comment or stripped_line.startswith('//'):
                continue
            
            # Count non-blank lines that are not comments
            if stripped_line and not stripped_line.startswith('//'):
                code_lines += 1
    return code_lines

def count_loops(filepath):
    """Count different levels of 'for' loop nesting and 'while' loops."""
    nesting_counts = [0] * 5  # Holds counts for 'for' loops from level 1 to 5
    while_count = 0
    current_nesting_level = 0

    with open(filepath, 'r') as file:
        for line in file:
            stripped_line = line.strip()

            # Count while loops
            if re.match(r'^\s*while\s*\(', stripped_line):
                while_count += 1

            # Check for opening and closing braces to track nesting
            if '{' in stripped_line:
                if re.search(r'\bfor\s*\(', stripped_line):
                    current_nesting_level += 1
                    if current_nesting_level <= 5:
                        nesting_counts[current_nesting_level - 1] += 1
            if '}' in stripped_line:
                if current_nesting_level > 0:
                    current_nesting_level -= 1

    return nesting_counts, while_count

def analyze_c_files(directory):
    """Analyze each .c file and return a list of dictionaries with the results."""
    results = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.c'):
                filepath = os.path.join(root, file)
                code_lines = count_code_lines(filepath)
                for_counts, while_count = count_loops(filepath)

                results.append({
                    'File': filepath,
                    'Lines of Code': code_lines,
                    '1st Level For Loops': for_counts[0],
                    '2nd Level For Loops': for_counts[1],
                    '3rd Level For Loops': for_counts[2],
                    '4th Level For Loops': for_counts[3],
                    '5th Level For Loops': for_counts[4],
                    'While Loops': while_count
                })
    return results

def write_csv(data, output_file):
    """Write data to a CSV file."""
    headers = [
        'File', 'Lines of Code', '1st Level For Loops', '2nd Level For Loops',
        '3rd Level For Loops', '4th Level For Loops', '5th Level For Loops', 'While Loops'
    ]

    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)

# Directory to analyze and output file name
directory_path = '/path/to/your/folder'
output_csv = 'c_file_analysis.csv'

# Run the analysis and save to CSV
results = analyze_c_files(directory_path)
write_csv(results, output_csv)

print(f"Analysis complete. Results saved to '{output_csv}'.")
