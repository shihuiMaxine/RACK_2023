import requests
import re
# Replace 'raw_url' with the raw URL of the file
raw_url = 'https://raw.githubusercontent.com/apache/airflow/09880741cbfc4c1e6d433d1e7fac60deccd10a97/dev/send_email.py'
raw_url='https://raw.githubusercontent.com/django/django/594873befbbec13a2d9a048a361757dd3cf178da/django/contrib/auth/hashers.py'
response = requests.get(raw_url)
code = response.text
import re

def extract_method_names(code):
    method_pattern = re.compile(r'\bdef\s+([a-zA-Z_]\w*)\s*\(')
    matches = method_pattern.findall(code)
    return matches

# Your example code
example_code = code

# Extract method names
method_names = extract_method_names(example_code)

# Print the result
# print(method_names)

# print(code)
f = open("examplecode.txt", "r")
content1=""
for line in f:
    content1+=line
print(content1)
pattern = r"\w+\("
method_names = re.findall(pattern, content1)
list1=[]
string1=""
for name in method_names:
    nameele=name[0:len(name)-1]
    if nameele not in list1:
        if nameele != "print":
            list1.append(nameele)
            string1+=nameele
            string1+=" "
print(list1)
# file_name = 'output.txt'
# with open(file_name, 'w') as txt_file:
#     txt_file.writelines(list1)
import ast
totalapi=[]
import ast

class MethodNameExtractor(ast.NodeVisitor):
    def __init__(self):
        self.method_names = []

    def visit_FunctionDef(self, node):
        self.method_names.append(node.name)
        self.generic_visit(node)

def extract_method_names(code):
    tree = ast.parse(code)
    extractor = MethodNameExtractor()
    extractor.visit(tree)
    return extractor.method_names

# Your example code
example_code = code

# Extract method names
method_names = extract_method_names(example_code)

# Print the result
# print(method_names)
# class APITraverser(ast.NodeVisitor):
#     def __init__(self):
#         self.api_methods = set()

#     def visit_FunctionDef(self, node):
#         # Extract function names
#         # print(node.name)
#         if node.name not in totalapi:
#             totalapi.append(node.name)


#         self.api_methods.add(("function", node.name))
#         self.generic_visit(node)

#     def visit_ClassDef(self, node):
#         # Extract method names inside classes
#         for item in node.body:
#             if isinstance(item, ast.FunctionDef):
#                 # print(node.name)
#                 # print(item.name)
#                 if node.name not in totalapi:
#                     totalapi.append(node.name)
#                 if item.name not in totalapi:
#                     totalapi.append(item.name)
#                 # print(f"{node.name}.{item.name}")
#                 self.api_methods.add(("method", f"{node.name}.{item.name}"))
#                 # self.api_methods.add(("method", f"{item.name}"))

#         self.generic_visit(node)

# def extract_api_from_code(code):
#     tree = ast.parse(code)
#     traverser = APITraverser()
#     traverser.visit(tree)
#     return traverser.api_methods

# # Example code
# example_code = code

# api_methods = extract_api_from_code(example_code)
# print(api_methods)
# print(totalapi)
k=['hexdigest', 'md5', 'encode', 'update']
cal=0
for i in k:
    
    if i in list1:
        print(i)
        cal +=1
per = cal/(len(list1)+(len(k)-cal))
# print(per)