import ast

# Your Python code snippet
code = """
def send_email(to, subject, body):
    # Actual implementation of send_email
    print(f"Sending email to {to} with subject '{subject}' and body '{body}'")

send_email("user@example.com", "Hello", "This is the email body")
"""

class ApiExtractor(ast.NodeVisitor):
    def visit_Call(self, node):
        if isinstance(node.func, ast.Name):
            # Function call without any object, e.g., function()
            if node.func.id == "send_email":
                print("Found 'send_email' method call:")
                print(ast.get_source_segment(node, code))

        elif isinstance(node.func, ast.Attribute) and isinstance(node.func.value, ast.Name):
            # Method call, e.g., object.method()
            if node.func.attr == "send_email":
                print("Found 'send_email' method call:")
                print(ast.get_source_segment(node, code))

# Parse the code and visit the AST nodes
tree = ast.parse(code)
extractor = ApiExtractor()
extractor.visit(tree)




