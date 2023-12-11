import ast
import re
import csv
file = open("data_codeapi.csv")

print(type(file))
csvreader = csv.reader(file)
k=['MIMEText', 'sendmail','SMTP','MIMEMultipart','login']
totalweb=[]
totalapi=[]
totalcode=[]
n=0
for row in csvreader:
    if n !=0:
        web1=row[0]
        api1=row[1]
        code1=row[2]
        totalweb.append(web1)
        totalapi.append(api1)
        totalcode.append(code1)
    n+=1



tree = ast.parse(totalcode[1])
target_name = "sendemail"

for node in ast.walk(tree):
    if (
        isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and
        (node.name == target_name or
         (isinstance(node, ast.Call) and hasattr(node.func, 'id') and node.func.id == target_name) or
         (isinstance(node, ast.Attribute) and hasattr(node.value, 'id') and node.value.id == target_name)
        )
    ):
        print(ast.get_source_segment(totalcode[1], node))