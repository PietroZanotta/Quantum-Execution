# from pycparser import c_parser, c_ast, c_generator

# class FunctionCallInliner(c_ast.NodeVisitor):
#     def __init__(self, function_definitions):
#         self.function_definitions = function_definitions

#     def visit_FuncCall(self, node):
#         # Check if the function call is for one of the defined functions
#         if node.name.name in self.function_definitions:
#             function_decl, function_body = self.function_definitions[node.name.name]
#             # Substitute the parameters in the function body with actual values passed in the call
#             return self.inline_function_body(function_decl, function_body, node)
#         return node

#     def inline_function_body(self, function_decl, function_body, func_call_node):
#         # Extract the parameter names from the function declaration
#         param_name = function_decl.type.args.params[0].name  # Assuming 1 argument (simplified for this example)
#         arg_value = func_call_node.args.exprs[0]

#         # Create a new visitor to replace the parameter with the argument
#         class ParamReplacer(c_ast.NodeVisitor):
#             def visit_ID(self, node):
#                 if node.name == param_name:
#                     return c_ast.Constant(type="int", value=str(arg_value))
#                 return node

#         replacer = ParamReplacer()
#         replacer.visit(function_body)

#         # Return the modified function body as a list of statements
#         return function_body.block_items

# def extract_functions(c_code):
#     """
#     Extract function definitions from C code and return a dictionary of function name -> (function declaration, function body).
#     """
#     parser = c_parser.CParser()
#     ast = parser.parse(c_code)
#     function_definitions = {}

#     for ext in ast.ext:
#         # print(ext)
#         # print("\n\n\n")
#         if isinstance(ext, c_ast.FuncDef):
#             function_name = ext.decl.name
#             function_decl = ext.decl
#             # print(ext.decl.type)
#             # print(dir(ext.decl.type.type))
#             function_body = ext.body
#             function_definitions[function_name] = (function_decl, function_body)

#     return function_definitions

# def inline_function_calls(c_code):
#     """
#     Inline all function calls in the code with the corresponding function bodies.
#     """
#     parser = c_parser.CParser()
#     ast = parser.parse(c_code)
#     function_definitions = extract_functions(c_code)

#     # Use the visitor to inline function calls with their body
#     inliner = FunctionCallInliner(function_definitions)
#     inliner.visit(ast)
#     print(dir(inliner.visit(ast)))

#     # Use the generator to convert the modified AST back to C code
#     generator = c_generator.CGenerator()
#     modified_code = generator.visit(ast)

#     return modified_code

# # Example usage
# c_code = """
# inline void doStuff(int a){
#     int b;
#     b = a;
# }

# int main(){
#     int x;
#     x = 1;
#     doStuff(x);
#     return 0;
# }
# """

# modified_code = inline_function_calls(c_code)
# print(modified_code)


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
            for i in range(start_value, max_value + 1):
                new_var_assign = c_ast.Assignment(
                    op='=', 
                    lvalue=c_ast.ID(name=loop_var), 
                    rvalue=c_ast.Constant(type="int", value=str(i))
                )
                unrolled_statements.append(new_var_assign)
                body_copy = self.replace_loop_var(for_node.stmt, loop_var, i)
                unrolled_statements.extend(body_copy if isinstance(body_copy, list) else [body_copy])
        
        elif for_node.cond.op == ">=" or for_node.cond.op == ">":
            for i in reversed(range(max_value, start_value + 1)):
                new_var_assign = c_ast.Assignment(
                    op='=', 
                    lvalue=c_ast.ID(name=loop_var), 
                    rvalue=c_ast.Constant(type="int", value=str(i))
                )
                unrolled_statements.append(new_var_assign)
                body_copy = self.replace_loop_var(for_node.stmt, loop_var, i)
                unrolled_statements.extend(body_copy if isinstance(body_copy, list) else [body_copy])

        return unrolled_statements

    def replace_loop_var(self, node, var_name, value):
        class ReplaceVarVisitor(c_ast.NodeVisitor):
            def __init__(self, var_name, value):
                self.var_name = var_name
                self.value = value

            def visit(self, node):
                for child_name, child in node.children():
                    if isinstance(child, c_ast.ID) and child.name == self.var_name:
                        setattr(node, child_name, c_ast.Constant(type="int", value=str(self.value)))
                    elif isinstance(child, c_ast.ExprList):
                        for idx, expr in enumerate(child.exprs):
                            if isinstance(expr, c_ast.ID) and expr.name == self.var_name:
                                child.exprs[idx] = c_ast.Constant(type="int", value=str(self.value))
                    elif hasattr(child, 'children'):
                        self.visit(child)

        replace_visitor = ReplaceVarVisitor(var_name, value)
        replace_visitor.visit(node)
        return node

def extract_includes(c_code):
    include_lines = re.findall(r'^\s*#include\s+[<"][^">]+[">]', c_code, flags=re.MULTILINE)
    code_without_includes = re.sub(r'^\s*#include\s+[<"][^">]+[">]\s*', '', c_code, flags=re.MULTILINE)
    return include_lines, code_without_includes

def unroll_loops_in_code(c_code):
    include_lines, code_without_includes = extract_includes(c_code)
    include_text = "\n".join(include_lines) + "\n" if include_lines else ""
    
    parser = c_parser.CParser()
    ast = parser.parse(code_without_includes)

    unroll_visitor = UnrollForLoopsVisitor()
    unroll_visitor.visit(ast)

    generator = c_generator.CGenerator()
    modified_code = generator.visit(ast)
    
    modified_code_with_includes = include_text + modified_code
    return modified_code_with_includes

# Example usage
c_code = """
#include <stdio.h>

void doStuff(int a) {
  int b = a;
}

int main() {
    int i;
    int x;
    for (i = 4; i >= 4; i--) {
      x = i;
      doStuff(x);
    }

    for (i = 0; i <= 2; i++) {
      x = i;
      doStuff(x);
    }
    return 0;
}
"""

modified_code = unroll_loops_in_code(c_code)
print(modified_code)
