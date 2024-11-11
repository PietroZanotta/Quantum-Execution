from pycparser import c_parser, c_ast, c_generator
import re

class UnrollWhileLoopsVisitor(c_ast.NodeVisitor):
    def __init__(self, n):
        self.n = n  # Number of times to unroll the loop

    def visit_Compound(self, node):
        new_block_items = []
        for stmt in (node.block_items or []):
            if isinstance(stmt, c_ast.While) and self.n > 0:
                unrolled_statements = self.unroll_while_loop(stmt, self.n)
                new_block_items.extend(unrolled_statements)
            else:
                new_block_items.append(stmt)
        node.block_items = new_block_items
        self.generic_visit(node)

    def unroll_while_loop(self, while_node, n):
        unrolled_statements = []
        for i in range(n):
            condition = while_node.cond
            if_stmt = c_ast.If(cond=condition, iftrue=while_node.stmt, iffalse=None)
            unrolled_statements.append(if_stmt)
        return unrolled_statements

def extract_includes(c_code):
    # Extract #include lines from the code
    include_lines = re.findall(r'^\s*#include\s+[<"][^">]+[">]', c_code, flags=re.MULTILINE)
    # Remove the #include lines from the code for parsing
    code_without_includes = re.sub(r'^\s*#include\s+[<"][^">]+[">]\s*', '', c_code, flags=re.MULTILINE)
    return include_lines, code_without_includes

def unroll_while_loops_in_code(c_code, n):
    # Extract includes and code separately
    include_lines, code_without_includes = extract_includes(c_code)
    include_text = "\n".join(include_lines) + "\n" if include_lines else ""
    
    # Parse the code without includes
    parser = c_parser.CParser()
    ast = parser.parse(code_without_includes)
    
    # Unroll while loops in the AST
    unroll_visitor = UnrollWhileLoopsVisitor(n)
    unroll_visitor.visit(ast)
    
    # Generate the modified code
    generator = c_generator.CGenerator()
    modified_code = generator.visit(ast)
    
    # Combine includes with modified code
    modified_code_with_includes = include_text + modified_code
    return modified_code_with_includes

# Example usage
c_code_with_includes = """
#include <stdio.h>

void doStuff(int a){
  int b = a;
  printf("Value of b: %d\\n", b);
}

int main() {
    int i = 0;
    int x;
    while(myCondition(i)) {
      x = i + 2;
      doStuff(x);
      i=i+1;
    }

    return 0;
}
"""

modified_code = unroll_while_loops_in_code(c_code_with_includes, n=3)
print(modified_code)
