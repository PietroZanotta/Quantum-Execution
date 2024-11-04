import clang.cindex

clang.cindex.Config.set_library_file("/home/linuxbrew/.linuxbrew/opt/python@3.11/lib/python3.11/site-packages/clang/native/libclang.so")


# Sample C code as a string
code = """
int main() {
    int x = 42;
    prinf(x);
    return 0;
}
"""

# Write code to a temporary file
with open("temp.c", "w") as f:
    f.write(code)

# Load the Clang index and parse the file
index = clang.cindex.Index.create()
translation_unit = index.parse("temp.c")

# Define a function to traverse the AST and create a custom representation
class ASTNode():
    def __init__(self, kind, spelling, children=None):
        self.kind = kind
        self.spelling = spelling
        self.children = children if children is not None else []

    def __repr__(self, level=0):
        ret = "\t" * level + repr(self.spelling) + " (" + self.kind + ")\n"
        for child in self.children:
            ret += child.__repr__(level + 1)
        return ret

# Function to recursively copy the Clang AST to our custom ASTNode
def build_custom_ast(node):
    custom_node = ASTNode(kind=str(node.kind), spelling=node.spelling)
    for child in node.get_children():
        custom_node.children.append(build_custom_ast(child))
    return custom_node

# Build custom AST from the parsed Clang AST
custom_ast = build_custom_ast(translation_unit.cursor)
print("Original AST:")
print(custom_ast)

# Modify the custom AST by searching for '42' and replacing it with '100'
def modify_ast(node):
    if node.spelling == "42":
        node.spelling = "100"
    for child in node.children:
        modify_ast(child)

modify_ast(custom_ast)
print("\nModified AST:")
print(custom_ast)

# Generate the modified code from our custom AST
def generate_code(node):
    if node.kind == 'CursorKind.INTEGER_LITERAL' and node.spelling == "100":
        return "100"
    elif node.kind == 'CursorKind.VAR_DECL' and node.spelling == "x":
        return "int x = 100;"
    else:
        code = ""
        for child in node.children:
            code += generate_code(child)
        return code

print("\nGenerated Modified Code:")
print(generate_code(custom_ast))


# Generate the complete modified code from the custom AST
def generate_code(node):
    code = ""
    
    # Handle variable declarations
    if node.kind == 'CursorKind.VAR_DECL':
        code += f"int {node.spelling} = {node.children[0].spelling};\n"
    
    # Handle return statements
    elif node.kind == 'CursorKind.RETURN_STMT':
        code += f"    return {node.children[0].spelling};\n"

    # Handle the main function
    elif node.kind == 'CursorKind.FUNCTION_DECL':
        code += f"int {node.spelling}() {{\n"
        for child in node.get_children():
            code += generate_code(child)
        code += "}\n"
    
    # Recursively generate code for child nodes
    for child in node.children:
        code += generate_code(child)

    return code

# Generate the modified code using the custom AST
modified_code = generate_code(custom_ast)
print("\nGenerated Modified Code:")
print(modified_code)

# Write the modified code to a new C file
with open("modified_temp.c", "w") as f:
    f.write("#include <stdio.h>\n\n")
    f.write(modified_code)
    f.write("int main() {\n    return 0;\n}\n")

print("\nModified code has been written to 'modified_temp.c'.")