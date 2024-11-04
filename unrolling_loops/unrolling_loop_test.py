import clang.cindex

# Set up the library path for clang
clang.cindex.Config.set_library_file("/home/linuxbrew/.linuxbrew/opt/python@3.11/lib/python3.11/site-packages/clang/native/libclang.so")

def parse_c_code(code):
    index = clang.cindex.Index.create()
    translation_unit = index.parse('temp.c', args=['-std=c11'], unsaved_files=[('temp.c', code)])
    return translation_unit.cursor

# Sample C code
c_code = """
int main() {
    a = 0;
    a++;
    for(int i = 0; i <= 3; i++){
        printf("Loop iteration %d\\n", i);
    }
    // for (int i = 0; i < 3; i++) //{
    // printf("Loop iteration %d\\n", i);
    // }

    // while (i < 5){
    // i++;
    // }

  //  return 0;
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
    c = 0
    # Use the preorder walk to traverse the AST
    for node in cursor.walk_preorder():
        print(unfolded_code)
        print("\n\n")
        
        if c ==4:
            break
        c+=1
        
        if node.kind == clang.cindex.CursorKind.FOR_STMT:
#             # For loop handling
            children = list(node.get_children())
            # if len(children) < 4:
            #     continue  # Not enough children for a valid for loop

            init_stmt, cond_stmt, inc_stmt, body_stmt = children[:4]
            # for i in range(4):
            #     print(children[i].kind)
            
            # Get initialization token
            init_tokens = list(init_stmt.get_tokens())
            spelling_list=[]
            for token in init_tokens:
                spelling_list.append(token.spelling)

            start = int(spelling_list[3]) # assuming something like i = 0 initilizing the looping variable # assuming something like i = 0 initilizing the looping variable

            init_tokens = list(cond_stmt.get_tokens())
            spelling_list=[]
            for token in init_tokens:
                spelling_list.append(token.spelling)

            end = int(spelling_list[2])

            # Unfold loop by iterating manually
            print("unfolding")
            
            for i in range(start, end):
                unfolded_code += f"// Unfolded iteration number {i+1}\n"
                unfolded_code += f"int i = {i};\n"  # Declare the loop variable
                unfolded_code += extract_code_from_node(body_stmt)  # Extract the body code
                unfolded_code += "\n"  # Add a new line for readability

        elif node.kind == clang.cindex.CursorKind.WHILE_STMT:
            print("work in progess")
            # While loop handling (not implemented in this example)
            continue  # You can implement similar logic if needed

        else:
            if(node.children()):
                continue
            # For all other nodes, just extract their code representation
            unfolded_code += extract_code_from_node(node)

    return unfolded_code

# # Unfold loops in the C code
unfolded_c_code = unfold_loops(root)
# print(unfolded_c_code)

def print_ast(node, indent=2):
    # Print the node's kind, spelling, and location
    print("  " * indent + f"{node.kind} | {node.spelling} | {node.location}")
    
    # Recursively print each child node
    for child in node.get_children():
        print_ast(child, indent + 1)

# Print the AST
# print_ast(root)
