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

def find_code_with_method(text, method_name_total):
    lines = text.split('\n')
    found_code = []
    in_method_block = False

    for line in lines:
        # Check if the line contains the method name
        for method_name in method_name_total:
            if method_name in line:
                in_method_block = True
                code_snippet = [line]
            elif in_method_block:
                code_snippet.append(line)

        # Check if the method block ends
            if in_method_block and line.strip() == "":
                in_method_block = False
                found_code.append('\n'.join(code_snippet))

    return found_code

# Example usage:
your_text_with_code = """
def sendmail(subject, body, to):
    # Code for sending mail
    pass

# Other code here

def some_other_method():
    sendmail()
    # Code that does something else
    pass
"""

method_name_to_find = ['MIMEText', 'sendmail','SMTP','MIMEMultipart','login']
found_code_snippets = find_code_with_method(totalcode[0], method_name_to_find)

for snippet in found_code_snippets:
    print("Code snippet with method '{}' found:".format(method_name_to_find))
    print(snippet)
    print("-" * 40)