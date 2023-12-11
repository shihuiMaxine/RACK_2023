import requests
import ast
import re
import csv
import tokenize
from io import BytesIO

f = open("example.txt", "r")
# code = f.read()
totalweb=[]
dicta={}
lista=[]
listg=[]
listr=[]
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



def remove_comments_from_code(code):
    # Tokenize the code
    tokens = list(tokenize.tokenize(BytesIO(code.encode('utf-8')).readline))

    # Filter out comments
    new_tokens = [t for t in tokens if t.type != tokenize.COMMENT]

    # Reconstruct the code without comments
    modified_code = tokenize.untokenize(new_tokens).decode('utf-8')

    return modified_code

# Example usage
code_with_comments = """
# This is a comment
def example_function():
    # Another comment
    print("Hello, World!")

# Docstring for the function
class ExampleClass:
    '''This is a docstring.'''
    pass
"""

code_without_comments = remove_comments_from_code(code_with_comments)
# print(code_without_comments)

def remove_comments(input_code):
    # Use a regular expression to match and remove comments
    cleaned_code = re.sub(r'^\s*#.*|(""")[\s\S]*?\1|(\'\'\')[\s\S]*?\2', '', input_code)
    return cleaned_code

# Example usage:
input_code = """
# This is a single-line comment
print("Hello, world!")  # Another comment

"""
cleaned_code = remove_comments(input_code)
# print(cleaned_code)

# print(code_content)
def find_code_snippet(code_text, target_content):
    # print(code_text)
    code_without_comments = remove_comments_from_code(code_text)
    # Parse the code
    # print(code_without_comments)
    cleaned_code = remove_comments(code_text)
    # print(cleaned_code)
    # try:
    parsed_code = ast.parse(str(cleaned_code))
    # except:
    #     ast.parse(str(" "))
    # print()

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
    response = requests.get(github_url)
    response.raise_for_status() 
    raw_url=""
    if response.status_code == 200:

    
        # Construct the raw URL
        raw_url = f"https://raw.githubusercontent.com/{owner}/{repo}/{branch_or_commit}/{file_path}"
        response = requests.get(raw_url)
        response.raise_for_status() 
        if response.status_code == 200:

            return github_url,raw_url
        else:
            return "",""

    

# Example GitHub URL
giturllist=[]
for i in totalweb[0:5]:
    github_url = i

    # Convert to raw URL
    giturl,raw_url = github_url_to_raw_url(github_url)
    if giturl != "":
        totalraw.append(raw_url)
        giturllist.append(giturl)

    # Print the raw URL
    print(raw_url)

# print(totalweb[0])
headdata1=["website","raw_website","api","code","relative percents"]
listrtotal=[]
with open('web_api_code.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(headdata1)
    for q in range(0,len(totalraw)):
        j=totalraw[q]
        githuburl = giturllist[q]
        codecontent=[]
        apicontent=[]
        response = requests.get(j)
        
        code_content = response.text
        # Your input code
        input_code = code_content

        # Target content to find
        # target_content = 'SMTP'
        # k=['MIMEText', 'sendmail','SMTP','MIMEMultipart','login']
        # k=['hexdigest', 'md5', 'encode', 'update', 'hashlib']
        # k=["range", "gcd", "len", "int", "set"]
        # k=["execute", "len", "cursor", "append", "range"]
        k=['read_csv', 'open', 'pandas', 'append', 'DataFrame']
    
        # k=['MIMEMultipart']
        # Find the code snippets containing the target content
        for m in k:
            m1=(" "+m+"(") or("."+m+"(")
            m1=m+"("
            try:
                output_code_snippets =find_code_snippet(input_code, m1)
            except:
                break
            for i, snippet in enumerate(output_code_snippets, 1):
                print(f"Output {m}:\n{snippet}\n{'='*40}")
                if m not in apicontent:
                    apicontent.append(m)
                # print(apicontent)
                codecontent.append(f"{snippet}\n{'='*40}")
        if len(apicontent)!=0:
            datacontent1=[githuburl,j,apicontent,codecontent]
            totalcont.append(datacontent1)
            

            # writer.writerow(datacontent1)
    

    
    for i in range (0, len(k)):
        for x in totalcont:
            # print(x[0])
            if (len(k)-i ) == len(x[2]):
                # print(len(k)-i)
                # print(x[2])
                # print(x[0])
                response = requests.get(x[1])
                code = response.text
                pattern = r"\w+\("
                method_names = re.findall(pattern, code)
                list1=[]
                string1=""
                for name in method_names:
                    nameele=name[0:len(name)-1]
                    if nameele not in list1:
                        if nameele != "print":
                            list1.append(nameele)
                            string1+=nameele
                            string1+=" "
                totalnum=len(list1)+i
                perc=(len(x[2]))/(len(list1)+i)
                # print(list1)
                # print(perc)
                lista.append(perc)
                dicta[perc]=x



                
                # x.append(perc)


                # writer.writerow(x)
                    # writer.writerow(x)
    co =0
    # print(lista.sort())
    lista.sort(reverse=True)
    # print(dicta[0])
    # print(lista)
    for i in lista:
        listr=[]
        if co <5:
            # print(dicta[i])
            listr=dicta[i]
            # for j in dicta[i]:
            #     listr.append(j)
            listr.append(i)
            for z in listr[3]:
                # u=0
                print(z)
                listrtotal.append(z)
            writer.writerow(listr)
        co +=1







    pattern = r"\w+\("
    codedict={}
    list1tital=[] 
    listtotalcode=[]                    
    for i in listrtotal:
        list1=[]
        list2=[]
        listsame=[]
        # print(i)
        countapi=0
        method_names = re.findall(pattern, i)
        for name in method_names:
            if name[0:-1] not in list1:
                if name[0:-1] != "print":
                    list1.append(name[0:-1])
                    string1+=name[0:-1]
                    string1+=" "
                    # print(name[0:-1])
                    # k=["execute", "len", "cursor", "append", "range"]
                    if name[0:-1] in k:
                        countapi+=1
                        listsame.append(name[0:-1])


        list1tital.append(listsame)
        listtotalcode.append(i)
    for i in range (0, len(list1tital)-1):
        print(listtotalcode[i])
        print(list1tital[i])
        clean_code = remove_comments(listtotalcode[i])
        codedict[clean_code]=len(list1tital[i])

    sorted_dict_descending = dict(sorted(codedict.items(), key=lambda item: item[1], reverse=True))

    cn=0
    for i in list(sorted_dict_descending.keys()):
        if cn < 3:
            print(i)
            print(sorted_dict_descending[i])
            

        cn+=1