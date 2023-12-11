import requests
import ast
import re
import csv
f = open("example.txt", "r")
# code = f.read()
totalweb=[]
for i in f:
    # print(i.rstrip("\n"))
    totalweb.append(i.rstrip("\n"))

totalraw=[]
totalcont=[]
# file = open("data_codeapi.csv")

# print(type(file))
# csvreader = csv.reader(file)
# k=['MIMEText', 'sendmail','SMTP','MIMEMultipart','login']
# totalweb=[]
# totalapi=[]
# totalraw=[]
# n=0
# for row in csvreader:
#     if n !=0:
#         web1=row[0]
#         api1=row[1]
#         totalweb.append(web1)
#         totalapi.append(api1)
#     n+=1

# Replace 'raw_url' with the raw URL of the file
# for  orderurl in raw_url:
raw_url = 'https://raw.githubusercontent.com/apache/airflow/09880741cbfc4c1e6d433d1e7fac60deccd10a97/dev/send_email.py'
# raw_url = 'https://raw.githubusercontent.com/apache/airflow/blob/09880741cbfc4c1e6d433d1e7fac60deccd10a97/dev/send_email.py'


# print(code_content)
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


# raw_url = 'https://raw.githubusercontent.com/vnpy/vnpy/dc60e24199b110509d144c39d05280d43a5be0ed/vnpy/trader/engine.py'

# response = requests.get(raw_url)
# code_content = response.text

# print(code_content)
# import requests

def github_url_to_raw_url(github_url):
    # Parse the GitHub URL
    parts = github_url.split("/")
    
    # Extract the repository owner, repository name, and branch or commit hash
    owner, repo, branch_or_commit = parts[3], parts[4], parts[6]
    
    # Extract the path to the file
    file_path = "/".join(parts[7:])
    
    # Construct the raw URL
    raw_url = f"https://raw.githubusercontent.com/{owner}/{repo}/{branch_or_commit}/{file_path}"
    
    return github_url,raw_url

# Example GitHub URL
giturllist=[]
for i in totalweb:
    github_url = i

    # Convert to raw URL
    giturl,raw_url = github_url_to_raw_url(github_url)
    totalraw.append(raw_url)
    giturllist.append(giturl)

    # Print the raw URL
    print(raw_url)

# print(totalweb[0])
headdata1=["website","raw_website","api","code"]

with open('web_api_code2.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(headdata1)
    for q in range(0,3):
        j=totalraw[q]
        githuburl = giturllist[q]
        codecontent=[]
        apicontent=[]
        response = requests.get(j)
        code_content = response.text
        # Your input code
        input_code = code_content

        # Target content to find
        target_content = 'SMTP'
        k=['MIMEText', 'sendmail','SMTP','MIMEMultipart','login']
        # k=['MIMEMultipart']
        # Find the code snippets containing the target content
        for m in k:
            m1=("."+ m+"(")or(" "+m+"(")
            # m2=m+"("
            output_code_snippets =find_code_snippet(input_code, m1)
            for i, snippet in enumerate(output_code_snippets, 1):
                print(f"Output {m}:\n{snippet}\n{'='*40}")
                if m not in apicontent:
                    apicontent.append(m)
                codecontent.append(f"Output {m}:\n{snippet}\n{'='*40}")
        if len(apicontent)!=0:
            datacontent1=[githuburl,j,apicontent,codecontent]
            totalcont.append(datacontent1)
            

            # writer.writerow(datacontent1)
    for i in range (0, len(k)):
        for x in totalcont:
            # print(x[0])
            if (len(k)-i ) == len(x[2]):
                print(len(k)-i)
                print(x[2])
                print(x[0])
                writer.writerow(x)
                    # writer.writerow(x)