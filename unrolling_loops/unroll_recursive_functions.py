from pycparser import c_parser, c_ast, c_generator
import re

class UnrollRecursiveFunctionsVisitor(c_ast.NodeVisitor):
    def __init__(self, function_name, unroll_depth):
        self.function_name = function_name
        self.unroll_depth = unroll_depth

    def visit_FuncDef(self, node):
        # Check if this is the function we want to unroll
        if node.decl.name == self.function_name:
            # Unroll the function body up to the specified depth
            unrolled_body = self.unroll_recursive_body(node.body, self.unroll_depth)
            node.body = c_ast.Compound(unrolled_body)

    def unroll_recursive_body(self, body_node, depth):
        """
        Recursively unrolls all instances of the recursive function call within the body.
        """
        if depth == 0:
            # Base case: Stop unrolling if we've reached the max depth
            return [c_ast.Return(c_ast.Constant(type="int", value="0"))]  # Don't know how to generalize this

        new_statements = []
        
        for stmt in body_node.block_items:
            print(stmt)
            if isinstance(stmt, c_ast.FuncCall) and stmt.name.name == self.function_name:
                # Recursive function call found; unroll it by adding the body again with decremented depth
                new_statements.extend(self.unroll_recursive_body(body_node, depth - 1))
            elif isinstance(stmt, c_ast.Compound):
                # Compound statements (like blocks) require further exploration
                nested_block = c_ast.Compound(self.unroll_recursive_body(stmt, depth))
                new_statements.append(nested_block)
            elif isinstance(stmt, c_ast.If):
                # Handle 'if' statements by unrolling in both branches
                stmt.iftrue = c_ast.Compound(self.unroll_recursive_body(stmt.iftrue, depth))
                if stmt.iffalse:
                    stmt.iffalse = c_ast.Compound(self.unroll_recursive_body(stmt.iffalse, depth))
                new_statements.append(stmt)
            elif isinstance(stmt, c_ast.Return):
                # Special handling for `Return` statements to explore nested recursive calls
                stmt.expr = self.unroll_recursive_expression(stmt.expr, depth)
                new_statements.append(stmt)
            else:
                # For non-recursive function calls or other statements, add them as-is
                # print(c_ast.Compound(stmt))
                # print("\n\n")
                new_statements.append(stmt)

        return new_statements

    def unroll_recursive_expression(self, expr, depth):
        """
        Recursively unrolls expressions containing the recursive function call, such as in Return or BinaryOp.
        """
        if isinstance(expr, c_ast.FuncCall) and expr.name.name == self.function_name:
            # Replace the recursive call with an unrolled body
            unrolled_body = self.unroll_recursive_body(c_ast.Compound([expr]), depth - 1)
            return c_ast.Compound(unrolled_body)  # Return as a Compound node
        elif isinstance(expr, c_ast.BinaryOp):
            # print(expr.left)
            # Recursively unroll the left and right sides of BinaryOp
            expr.left = self.unroll_recursive_expression(expr.left, depth)
            expr.right = self.unroll_recursive_expression(expr.right, depth)
        elif isinstance(expr, c_ast.ExprList):
            # Recursively unroll each expression in ExprList
            expr.exprs = [self.unroll_recursive_expression(e, depth) for e in expr.exprs]
        return expr

def unroll_recursive_functions_in_code(c_code, function_name, unroll_depth):
    # Remove preprocessor directives for simplicity
    c_code = re.sub(r'^\s*#.*$', '', c_code, flags=re.MULTILINE)
    parser = c_parser.CParser()
    ast = parser.parse(c_code)

    # Create a visitor for unrolling recursive functions
    unroll_visitor = UnrollRecursiveFunctionsVisitor(function_name, unroll_depth)
    unroll_visitor.visit(ast)

    generator = c_generator.CGenerator()
    modified_code = generator.visit(ast)

    return modified_code

# Example usage
c_code = """
#include <stdio.h>

int doStuff(int a) {
    while (a>10){return 12;}

    if (a == 1) {
        return 1;
    } else {

        doStuff(a - 1);
    }
}

int main() {
    int x;
    int y;
    x = 1;
    y = doStuff(x);
    return 0;
}
"""

modified_code = unroll_recursive_functions_in_code(c_code, function_name="doStuff", unroll_depth=2)
print(modified_code)
