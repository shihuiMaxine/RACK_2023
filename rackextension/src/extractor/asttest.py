import ast
f1 = open("codeex1.txt", "r")
code1 = f1.read()
print(type(code1))
rankapilist=["send_email","send_messages","logging","is_valid"]
class NameExtractor(ast.NodeVisitor):
    def visit_FunctionDef(self, node):
        print("Function name:", node.name)
        if (node.name in rankapilist):
            print("code:")
            print(ast.get_source_segment(code1, node))
            # print(node._attributes)

class ApiExtractor(ast.NodeVisitor):
    
    def visit_Call(self, node):
        if isinstance(node.func, ast.Name):
            # Function call without any object, e.g., function()
            print("Function call:", node.func.id)
            if (node.func.id in rankapilist):
                print("code:")
                print(ast.get_source_segment(code1, node))
                
        elif isinstance(node.func, ast.Attribute) and isinstance(node.func.value, ast.Name):
            # Method call, e.g., object.method()
            print("Method call:", node.func.value.id + "." + node.func.attr)
            if (node.func.value.id in rankapilist):
                print("code:")
                print(ast.get_source_segment(code1, node))
            if (node.func.attr in rankapilist):
                print("code:")
                print(ast.get_source_segment(code1, node))
            


# Parse the code and visit the AST nodes
tree = ast.parse(code1)
extractor = NameExtractor()
extractor.visit(tree)
extractor = ApiExtractor()
extractor.visit(tree)