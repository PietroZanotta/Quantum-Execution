import clang.cindex

# Set up the library path for clang
clang.cindex.Config.set_library_file("/home/linuxbrew/.linuxbrew/opt/python@3.11/lib/python3.11/site-packages/clang/native/libclang.so")

def parse_c_code(code):
    index = clang.cindex.Index.create()
    translation_unit = index.parse('temp.c', args=['-std=c11'], unsaved_files=[('temp.c', code)])
    return translation_unit.cursor

# Sample C code
c_code = """
// #include <stdio.h>

int main() {
    for (int i = 0; i < 3; i++) {
        printf("Loop iteration %d\\n", i);
    }
    for (int i = 2; i < 7; i++) {
        printf("Loop iteration %d\\n", i);
    }

    return 0;
}
"""

# Generate the AST
root = parse_c_code(c_code)

def unfold_loops(cursor):
    unfolded_code = ""

    def extract_code_from_node(node):
        code = ""
        for token in node.get_tokens():
            code += token.spelling + " "
        return code.strip() + "\n"

    # Use the preorder walk to traverse the AST
    for node in cursor.walk_preorder():
        if node.kind == clang.cindex.CursorKind.FOR_STMT:
            # For loop handling
            children = list(node.get_children())
            if len(children) < 4:
                continue  # Not enough children for a valid for loop

            init_stmt, cond_stmt, inc_stmt, body_stmt = children[:4]

            # Get initialization token
            init_tokens = list(init_stmt.get_tokens())
            if init_tokens:
                # Attempt to parse the initialization for start value
                try:
                    # Try to find '=' and extract the initial value
                    for token in init_tokens:
                        if '=' in token.spelling:
                            start = int(token.spelling.split('=')[1].strip())
                            break
                    else:
                        continue  # No '=' found, skip this loop
                except (ValueError, IndexError):
                    continue  # Handle parsing errors gracefully

            # Get condition token
            cond_tokens = list(cond_stmt.get_tokens())
            if cond_tokens:
                try:
                    end = int(cond_tokens[0].spelling.split('<')[1].strip())  # Get the end condition value
                except (ValueError, IndexError):
                    continue  # Handle parsing errors gracefully

            # Unfold loop by iterating manually
            for i in range(start, end):
                unfolded_code += f"// Unfolded iteration {i}\n"
                unfolded_code += f"int i = {i};\n"  # Declare the loop variable
                unfolded_code += extract_code_from_node(body_stmt)  # Extract the body code
                unfolded_code += "\n"  # Add a new line for readability

        elif node.kind == clang.cindex.CursorKind.WHILE_STMT:
            # While loop handling (not implemented in this example)
            continue  # You can implement similar logic if needed

        else:
            # For all other nodes, just extract their code representation
            unfolded_code += extract_code_from_node(node)

    return unfolded_code

# Unfold loops in the C code
unfolded_c_code = unfold_loops(root)
print(unfolded_c_code)

def print_ast(node, indent=2):
    # Print the node's kind, spelling, and location
    print("  " * indent + f"{node.kind} | {node.spelling} | {node.location}")
    
    # Recursively print each child node
    for child in node.get_children():
        print_ast(child, indent + 1)

# Print the AST
print_ast(root)
