from pycparser import c_parser, c_ast, parse_file

class LoopUnroller(c_ast.NodeVisitor):
    def visit_For(self, node):
        # Check if we have a simple for loop to unroll
        if isinstance(node.init, c_ast.Decl) and isinstance(node.cond, c_ast.BinaryOp) and node.cond.op == '<':
            start_val = node.init.init.value  # Starting value of the loop variable
            end_val = node.cond.right.value   # Ending value for the loop variable
            if isinstance(node.next, c_ast.UnaryOp) and node.next.op == 'p++':  # Only handle simple i++ cases
                unrolled_body = []
                for i in range(int(start_val), int(end_val)):
                    for stmt in node.stmt.block_items:
                        # Create a deep copy of the statement and replace loop variable with its value
                        new_stmt = c_ast.ID(name=str(i))
                        unrolled_body.append(new_stmt)
                node.stmt.block_items = unrolled_body  # Replace the loop with unrolled statements

# Parse and unroll loops
parser = c_parser.CParser()
ast = parser.parse("""
void main() {
    for (int i = 0; i < 3; i++) {
        printf("%d\\n", i);
    }
}
""")

print(ast)
unroller = LoopUnroller()
unroller.visit(ast)


print(ast)
