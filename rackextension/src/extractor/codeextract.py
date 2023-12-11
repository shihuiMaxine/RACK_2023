import requests
from bs4 import BeautifulSoup
import ast

def extract_code_without_comments(url):
    # Fetch the webpage content
    response = requests.get(url)
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all <code> or <pre> tags (or any specific tag where code resides)
        code_snippets = soup.find_all('application/json')  # Adjust tags as per the website's structure
        print(code_snippet)
        code_without_comments = ""
        for code_snippet in code_snippets:
            code = code_snippet.get_text()
            
            # Parse and remove comments using AST
            tree = ast.parse(code)
            
            class RemoveComments(ast.NodeTransformer):
                def visit_Expr(self, node):
                    if isinstance(node.value, ast.Str):
                        return None
                    return node
            
            transformer = RemoveComments()
            tree = transformer.visit(tree)
            
            # Generate code without comments
            code_without_comments += compile(tree, filename='', mode='exec')
        
        return code_without_comments
    else:
        return None

# Replace 'url' with the specific website URL
url = 'https://github.com/getsentry/sentry/blob/71be02dca325de7c709503ddccc4a020a65272bc/src/sentry/tasks/email.py'  # Put the URL of the website here

code_without_comments = extract_code_without_comments(url)
print (code_without_comments)
if code_without_comments:
    
    exec(code_without_comments)

