from pycparser import c_parser, c_ast, c_generator

class FunctionCallInliner(c_ast.NodeVisitor):
    def __init__(self, function_definitions):
        self.function_definitions = function_definitions

    def visit_FuncCall(self, node):
        # Check if the function call is for one of the defined functions
        if node.name.name in self.function_definitions:
            function_decl, function_body = self.function_definitions[node.name.name]
            # Substitute the parameters in the function body with actual values passed in the call
            return self.inline_function_body(function_decl, function_body, node)
        return node

    def inline_function_body(self, function_decl, function_body, func_call_node):
        # Extract the parameter names from the function declaration
        param_name = function_decl.type.args.params[0].name  # Assuming 1 argument (simplified for this example)
        arg_value = func_call_node.args.exprs[0]

        # Create a new visitor to replace the parameter with the argument
        class ParamReplacer(c_ast.NodeVisitor):
            def visit_ID(self, node):
                if node.name == param_name:
                    return c_ast.Constant(type="int", value=str(arg_value))
                return node

        replacer = ParamReplacer()
        replacer.visit(function_body)

        # Return the modified function body as a list of statements
        return function_body.block_items

def extract_functions(c_code):
    """
    Extract function definitions from C code and return a dictionary of function name -> (function declaration, function body).
    """
    parser = c_parser.CParser()
    ast = parser.parse(c_code)
    function_definitions = {}

    for ext in ast.ext:
        # print(ext)
        # print("\n\n\n")
        if isinstance(ext, c_ast.FuncDef):
            function_name = ext.decl.name
            function_decl = ext.decl
            # print(ext.decl.type)
            # print(dir(ext.decl.type.type))
            function_body = ext.body
            function_definitions[function_name] = (function_decl, function_body)

    return function_definitions

def inline_function_calls(c_code):
    """
    Inline all function calls in the code with the corresponding function bodies.
    """
    parser = c_parser.CParser()
    ast = parser.parse(c_code)
    function_definitions = extract_functions(c_code)

    # Use the visitor to inline function calls with their body
    inliner = FunctionCallInliner(function_definitions)
    inliner.visit(ast)
    print(dir(inliner.visit(ast)))

    # Use the generator to convert the modified AST back to C code
    generator = c_generator.CGenerator()
    modified_code = generator.visit(ast)

    return modified_code

# Example usage
c_code = """
void doStuff(int a){
    int b;
    b = a;
}

int main(){
    int x;
    x = 1;
    doStuff(x);
    return 0;
}
"""

modified_code = inline_function_calls(c_code)
print(modified_code)
