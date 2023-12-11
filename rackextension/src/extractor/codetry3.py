import ast

def find_code_snippet(code_text, target_content):
    # Parse the code
    parsed_code = ast.parse(code_text)

    # Define a visitor class to traverse the AST
    class FindContentVisitor(ast.NodeVisitor):
        def __init__(self, target_content):
            self.target_content = target_content
            self.found_code = []

        def visit_FunctionDef(self, node):
            # Check if the function contains the target content
            function_code = ast.get_source_segment(code_text, node)
            if self.target_content in function_code:
                self.found_code.append(function_code)

    # Create an instance of the visitor
    visitor = FindContentVisitor(target_content)

    # Visit the AST
    visitor.visit(parsed_code)

    return visitor.found_code

# Your input code
input_code = """
def send_email(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    sendmail(msg)

def sendmail(msg):
    smtp = SMTP('smtp.example.com')
    smtp.login('username', 'password')
    smtp.sendmail('from@example.com', 'to@example.com', msg.as_string())

def compose_email(subject, body, attachment):
    msg = MIMEMultipart()
    msg.attach(MIMEText(body))
    msg['Subject'] = subject
    msg.attach(attachment)
    sendmail(msg)
"""

# Target content to find
target_content = 'MIMEMultipart'

# Find the code snippets containing the target content
output_code_snippets = find_code_snippet(input_code, target_content)

# Print the output
for i, snippet in enumerate(output_code_snippets, 1):
    print(f"Output {i}:\n{snippet}\n{'='*40}")


