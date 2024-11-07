from pycparser import c_parser, c_ast, c_generator
import re

class UnrollForLoopsVisitor(c_ast.NodeVisitor):
    def visit_Compound(self, node):
        new_block_items = []
        for stmt in (node.block_items or []):
            if isinstance(stmt, c_ast.For):
                # Attempt to unroll the for loop
                unrolled_statements = self.unroll_for_loop(stmt)
                if unrolled_statements is not None:
                    new_block_items.extend(unrolled_statements)
                else:
                    new_block_items.append(stmt)
            else:
                new_block_items.append(stmt)
        node.block_items = new_block_items
        self.generic_visit(node)

    def unroll_for_loop(self, for_node):
        if not isinstance(for_node.init, c_ast.Assignment) or not isinstance(for_node.init.rvalue, c_ast.Constant):
            return None
        loop_var = for_node.init.lvalue.name
        
        start_value = int(for_node.init.rvalue.value)
        if not isinstance(for_node.cond, c_ast.BinaryOp) or for_node.cond.left.name != loop_var:
            return None
        end_value = int(for_node.cond.right.value)
        
        inclusive = (for_node.cond.op == "<=" or for_node.cond.op == ">=")

        max_value = end_value if inclusive else end_value - 1
        unrolled_statements = []
        
        if for_node.cond.op == "<=" or for_node.cond.op == "<":
          # <= and i++
          for i in range(start_value, max_value + 1):
              # Redefine the loop variable `i` at the beginning of each unrolled iteration
              new_var_assign = c_ast.Assignment(
                  op='=', 
                  lvalue=c_ast.ID(name=loop_var), 
                  rvalue=c_ast.Constant(type="int", value=str(i))
              )
              unrolled_statements.append(new_var_assign)  # Add the redefinition of `i`
              
              # Now replace occurrences of `i` inside the loop body with the updated value
              body_copy = self.replace_loop_var(for_node.stmt, loop_var, i)
              unrolled_statements.extend(body_copy if isinstance(body_copy, list) else [body_copy])
        
        elif for_node.cond.op == ">=" or for_node.cond.op == ">":
          # >= and i--
          for i in reversed(range(max_value, start_value + 1)):
              # Redefine the loop variable `i` at the beginning of each unrolled iteration
              new_var_assign = c_ast.Assignment(
                  op='=', 
                  lvalue=c_ast.ID(name=loop_var), 
                  rvalue=c_ast.Constant(type="int", value=str(i))
              )
              unrolled_statements.append(new_var_assign)  # Add the redefinition of `i`
              
              # Now replace occurrences of `i` inside the loop body with the updated value
              body_copy = self.replace_loop_var(for_node.stmt, loop_var, i)
              unrolled_statements.extend(body_copy if isinstance(body_copy, list) else [body_copy])

        return unrolled_statements

    def replace_loop_var(self, node, var_name, value):
        """
        Replace all occurrences of `var_name` in `node` with the constant `value`.
        """
        # print("value: " + str(value))
        class ReplaceVarVisitor(c_ast.NodeVisitor):
            def __init__(self, var_name, value):
                self.var_name = var_name
                self.value = value

            def visit(self, node):
                # Traverse children and replace variable instances
                # print("\n\n")
                # print("len loops: " + str(len(node.children())))
                c =0
                for child_name, child in node.children():
                    c+=1
                    # print("iter: " + str(c))
                    # print("val: " + str(self.value))
                    if isinstance(child, c_ast.ID) and child.name == self.var_name:
                        # print("a")
                        # Replace the ID node with a Constant node
                        setattr(node, child_name, c_ast.Constant(type="int", value="i"))
                    elif isinstance(child, c_ast.ExprList):
                        # print("b")
                        # Iterate over elements in ExprList and replace variable if found
                        for idx, expr in enumerate(child.exprs):
                            if isinstance(expr, c_ast.ID) and expr.name == self.var_name:
                                child.exprs[idx] = c_ast.Constant(type="int", value="i")
                                # print("cambio in: " + str(self.value))
                    elif hasattr(child, 'children'):
                        # print("c")
                        # Recursively visit if the child has further nested children
                        self.visit(child)

        replace_visitor = ReplaceVarVisitor(var_name, value)
        replace_visitor.visit(node)
        return node


def unroll_loops_in_code(c_code):
    c_code = re.sub(r'^\s*#.*$', '', c_code, flags=re.MULTILINE)
    parser = c_parser.CParser()
    ast = parser.parse(c_code)

    unroll_visitor = UnrollForLoopsVisitor()
    unroll_visitor.visit(ast)

    generator = c_generator.CGenerator()
    modified_code = generator.visit(ast)

    return modified_code

# Example usage
c_code = """
#include <stdio.h>

int doStuff(a){
  printf(a);
}

int main() {
    int i;
    int x;
    for (i = 5; i >= 4; i--) {
      x = i;
      doStuff(x);
    }

    for (i = 0; i <= 1; i++) {
      x = i;
      doStuff(x);
    }

    return 0;
}
"""

modified_code = unroll_loops_in_code(c_code)
print(modified_code)
