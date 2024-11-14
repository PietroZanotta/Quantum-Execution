import os
import re

def analyze_and_clean_files():
    # Define the root folder as the current directory where this script is located
    root_folder = os.path.dirname(os.path.abspath(__file__))

    # Regular expression to match "= a", "> a", "< a", ">= a", "<= a", "== a" where "a" is a number
    pattern = re.compile(r'([><=!]=?)\s*(\d+)')

    for dirpath, dirnames, filenames in os.walk(root_folder):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)

            # If file is not a .c file, delete it
            if not filename.endswith('.c'):
                os.remove(filepath)
                print(f"Removed non-C file: {filepath}")
                continue

            # Check if the file contains any assignment with conditions involving numbers
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
                file_content = file.read()

                # Search for the pattern in the file content
                matches = pattern.findall(file_content)
                if any(
                    (op == '=' and int(value) > 7) or
                    (op == '>' and int(value) <= 7) or
                    (op == '<' and int(value) >= 7) or
                    (op == '>=' and int(value) < 7) or
                    (op == '<=' and int(value) > 7) or
                    (op == '==' and int(value) == 7)
                    for op, value in matches
                ):
                    # If any assignment matches the condition, delete the file
                    os.remove(filepath)
                    print(f"Removed C file with forbidden assignment: {filepath}")

if __name__ == "__main__":
    analyze_and_clean_files()
