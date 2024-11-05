# from pycparser import c_parser, c_ast, parse_file

# class LoopUnroller(c_ast.NodeVisitor):
#     def visit_For(self, node):
#         # Check if we have a simple for loop to unroll
#         if isinstance(node.init, c_ast.Decl) and isinstance(node.cond, c_ast.BinaryOp) and node.cond.op == '<':
#             start_val = node.init.init.value  # Starting value of the loop variable
#             end_val = node.cond.right.value   # Ending value for the loop variable
#             if isinstance(node.next, c_ast.UnaryOp) and node.next.op == 'p++':  # Only handle simple i++ cases
#                 unrolled_body = []
#                 for i in range(int(start_val), int(end_val)):
#                     for stmt in node.stmt.block_items:
#                         # Create a deep copy of the statement and replace loop variable with its value
#                         # Assuming 'i' is used in the printf
#                         new_stmt = c_ast.FuncCall(
#                             name=c_ast.ID(name="printf"),
#                             args=c_ast.ExprList(exprs=[c_ast.Constant(type="string", value='"%d\\n"'),
#                                                         c_ast.Constant(type="int", value=str(i))])
#                         )
#                         unrolled_body.append(new_stmt)
#                 node.stmt.block_items = unrolled_body  # Replace the loop with unrolled statements

# class CCodeGenerator(c_ast.NodeVisitor):
#     def __init__(self):
#         self.code = ""

#     def visit_Constant(self, node):
#         self.code += node.value

#     def visit_ID(self, node):
#         self.code += node.name

#     def visit_Decl(self, node):
#         self.code += f"{node.type.type} {node.name} = {node.init};\n"

#     def visit_FuncCall(self, node):
#         self.code += f"{node.name.name}("
#         self.visit(node.args)
#         self.code += ");\n"

#     def visit_ExprList(self, node):
#         for i, expr in enumerate(node.exprs):
#             if i > 0:
#                 self.code += ", "
#             self.visit(expr)

#     def visit_Compound(self, node):
#         self.code += "{\n"
#         for stmt in node.block_items:
#             self.visit(stmt)
#         self.code += "}\n"

#     def visit_FuncDef(self, node):
#         self.visit(node.decl)
#         self.visit(node.body)

#     def visit_FileAST(self, node):
#         for ext in node.ext:
#             self.visit(ext)

#     def generate_code(self, node):
#         self.visit(node)
#         return self.code

# # Parse and unroll loops
# parser = c_parser.CParser()
# ast = parser.parse("""
# void main() {
#     for (int i = 0; i < 3; i++) {
#         printf("%d\\n", i);
#     }
# }
# """)
# unroller = LoopUnroller()
# unroller.visit(ast)

# # Generate new C code
# generator = CCodeGenerator()
# new_code = generator.generate_code(ast)
# print(new_code)


from pycparser import c_parser, c_ast, parse_file

class LoopUnroller(c_ast.NodeVisitor):
    def visit_For(self, node):
        # Check if we have a simple for loop to unroll
        if isinstance(node.init, c_ast.Decl) and isinstance(node.cond, c_ast.BinaryOp) and node.cond.op == '<':
            start_val = int(node.init.init.value)  # Starting value of the loop variable
            end_val = int(node.cond.right.value)   # Ending value for the loop variable
            if isinstance(node.next, c_ast.UnaryOp) and node.next.op == 'p++':  # Only handle simple i++ cases
                unrolled_body = []
                for i in range(start_val, end_val):
                    for stmt in node.stmt.block_items:
                        # Replace loop variable in the statement with its value
                        if isinstance(stmt, c_ast.FuncCall):
                            def curr(x):
                                print("aspetta un secondo")

                            new_stmt = c_ast.FuncCall(
                                name=c_ast.ID(name=stmt.name.name),
                                args=c_ast.ExprList(
                                    exprs=[
                                        c_ast.Constant(type="string", value='"%d\\n"'),
                                        c_ast.Constant(type="int", value=str(i))
                                    ]
                                )
                            )
                            unrolled_body.append(new_stmt)
                node.stmt.block_items = unrolled_body  # Replace loop with unrolled statements

class CCodeGenerator(c_ast.NodeVisitor):
    def __init__(self):
        self.code = ""

    def visit_FileAST(self, node):
        for ext in node.ext:
            self.visit(ext)

    def visit_FuncDef(self, node):
        self.visit(node.decl)
        self.visit(node.body)

    def visit_Decl(self, node):
        self.code += "dioporcor"#f"{' '.join(node.type.type)}" + f"{node.name}"
        if node.init:
            self.code += f" = {node.init.value}"
        self.code += ";\n"

    def visit_Compound(self, node):
        self.code += "{\n"
        for item in node.block_items:
            self.visit(item)
        self.code += "}\n"

    def visit_For(self, node):
        self.code += "for ("
        self.visit(node.init)
        self.visit(node.cond)
        self.visit(node.next)
        self.code += ") "
        self.visit(node.stmt)

    def visit_FuncCall(self, node):
        self.code += f"{node.name.name}("
        if node.args:
            for i, arg in enumerate(node.args.exprs):
                if i > 0:
                    self.code += ", "
                self.visit(arg)
        self.code += ");\n"

    def visit_Constant(self, node):
        self.code += node.value

    def visit_ID(self, node):
        self.code += node.name

    def visit_BinaryOp(self, node):
        self.visit(node.left)
        self.code += f" {node.op} "
        self.visit(node.right)

    def generate_code(self, node):
        self.visit(node)
        return self.code

# Parse and unroll loops
parser = c_parser.CParser()
ast = parser.parse("""
void main() {
    for (int i = 0; i < 3; i++) {
        printf("%d\\n", i);
    }
}
""")
unroller = LoopUnroller()
unroller.visit(ast)

# Generate new C code
generator = CCodeGenerator()
new_code = generator.generate_code(ast)
print(new_code)
