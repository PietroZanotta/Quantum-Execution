import pickle
from pycparser import c_parser

# Sample C code
c_code = """
int main() {
    int a = 0;
    a++;

    for (int i = 0; i <= 3; i++) {
        printf("Loop iteration %d\\n", i);
    }

    return 0;
}
"""

# Parse the C code to get the AST
parser = c_parser.CParser()
ast = parser.parse(c_code)

# Save the AST to a .ast file
with open("example.ast", "wb") as f:
    pickle.dump(ast, f)

print("AST has been saved to example.ast.")
