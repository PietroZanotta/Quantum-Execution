import ast
import astor

class LoopUnroller(ast.NodeTransformer):
    def visit_For(self, node):
        # Only unroll if the loop range can be determined
        if isinstance(node.iter, ast.Call) and isinstance(node.iter.func, ast.Name) and node.iter.func.id == 'range':
            if len(node.iter.args) == 1 and isinstance(node.iter.args[0], ast.Constant):
                end = node.iter.args[0].value
                unrolled_body = []
                
                # Generate the unrolled statements
                for i in range(end):
                    for stmt in node.body:
                        # Clone the statement and replace loop variable with current value
                        new_stmt = ast.fix_missing_locations(ast.NodeTransformer().visit(astor.to_source(stmt).replace(node.target.id, str(i))))
                        unrolled_body.append(new_stmt)
                
                return unrolled_body  # Replace the for loop with unrolled statements
        
        return node  # Leave unchanged if conditions aren't met

# Example code to unroll
code = """
for i in range(3):
    print(i)
"""

# Parse, transform, and unparse code
tree = ast.parse(code)

print(tree)
unroller = LoopUnroller()
new_tree = unroller.visit(tree)
new_code = ast.unparse(new_tree)

print(new_code)
