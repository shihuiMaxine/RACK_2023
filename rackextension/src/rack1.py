import rack
from rack import main
import ast
import sys
import extractor
import extractor.GitHubClient
import requests
from bs4 import BeautifulSoup
import re
import csv

totalcont=[]
lista=[]

dicta={}
listallcode=[]
print (sys.argv[2:])
stringquery=' '.join(sys.argv[2:])
print(stringquery)

question="https://api.github.com/search/code?q="
listquery=stringquery.split(" ")
for i in range (0, len(listquery)):
    question+=listquery[i] + "+"

question += "in:file+language:python"

call_url ="https://api.github.com/search/code?q=Accessing+a+list+of+rows+from+mySQL+table+in:file+language:python"
result = extractor.GitHubClient.execute_github_call(call_url)
htmlresult=result.split(",")
listgit=[]
numberurl=0
for i in htmlresult:
    if "html_url" in i:
        if ".py" in i:
            if numberurl < 5:
                listgit.append(i[12:len(i)-1])
                numberurl+=1

apitoken=main.main(stringquery)


k=apitoken
def github_url_to_raw_url(github_url):

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
        # print(raw_url)
        if response.status_code == 200:

            return github_url,raw_url
        else:
            return "",""

giturllist=[]
totalraw=[]
n=0
for i in listgit:
    github_url = i

    # Convert to raw URL
    giturl,raw_url = github_url_to_raw_url(github_url)
    if giturl != "":
        totalraw.append(raw_url)
        giturllist.append(giturl)


def remove_comments(input_code):
    # Use a regular expression to match and remove comments
    cleaned_code = re.sub(r'^\s*#.*|(""")[\s\S]*?\1|(\'\'\')[\s\S]*?\2', '', input_code)
    return cleaned_code
def remove_comments2(code):
    # Regular expression to match Python comments
    comment_pattern = r'#.*?$|(\'\'\'[\s\S]*?\'\'\'|\"\"\"[\s\S]*?\"\"\")'

    # Remove comments using re.sub
    code_without_comments = re.sub(comment_pattern, '', code, flags=re.MULTILINE)

    return code_without_comments
codelist=[]
for q in range(0,len(totalraw)):
    j=totalraw[q]
    githuburl = giturllist[q]
    codecontent=[]
    apicontent=[]
    response = requests.get(j)
    
    code_content = response.text
    # Your input code
    input_code = remove_comments2(code_content)

    # if q == 0:
    #     print(input_code)
    codelist.append(input_code)

def extract_functions_with_code(code):

    try: 
        tree = ast.parse(code)

        # Function to extract function nodes from the AST
        def get_function_nodes(node):
            if isinstance(node, ast.FunctionDef):
                return [node]
            else:
                return sum((get_function_nodes(child) for child in ast.iter_child_nodes(node)), [])

        # Get all function nodes from the AST
        try:
            function_nodes = get_function_nodes(tree)
        except:
            print("error")

        # Extract code snippets for each function
        function_code_snippets = []
        for node in function_nodes:
            try:
                code_snippet = ast.get_source_segment(code, node)
                function_code_snippets.append(code_snippet)
            except:
                print("error")

        return function_code_snippets
    except:
        listempty=[]
        return listempty
nun=0
for x in codelist:
    nun+=1
    code_snippet=x
    # print(nun)
    # Extract function code snippets from the code snippet
    function_code_snippets = extract_functions_with_code(code_snippet)
    # Print the extracted function code snippets
    for i, code_snippet in enumerate(function_code_snippets, 1):
        # print(f"Function {i} code snippet:")
        # print(code_snippet)
        listallcode.append(code_snippet)
        
        # print("-" * 30)
pattern = r"\w+\("
codedict={}
codedictm={}
codedictsame={}
list1tital=[] 
listtotalcode=[] 

for i in listallcode:
    list1=[]
    list2=[]
    listsame=[]
    countapi=0

    method_names = re.findall(pattern, i)
    for name in method_names:
        if name[0:-1] not in list1:
            if name[0:-1] != "print":
                list1.append(name[0:-1])

                k=apitoken
                if name[0:-1] in k:
                    if name[0:-1] not in listsame:
                        countapi+=1
                        listsame.append(name[0:-1])
    codedictm[i]=list1
    codedictsame[i]=listsame
    codedict[i]=len(listsame)

dictorder={}
for j in list(codedictsame.keys()):
    if len(codedictsame[j])>0:
        difapi=len(codedictm[j])+5-(len(codedictsame[j]))
        saapi=len(codedictsame[j])
        perc=saapi/difapi
        dictorder[j]=perc



my_dict = {'apple': 5, 'banana': 2, 'orange': 8, 'grape': 3}

sorted_dict_descending = dict(sorted(dictorder.items(), key=lambda item: item[1], reverse=True))

cn=0
for i in list(sorted_dict_descending.keys()):
    if cn < 5:
        print("#"+ str(cn+1))
        print(i)
        print(codedictm[i])
        print(codedictsame[i])
        print(sorted_dict_descending[i])
        print("#" * 60)
        

    cn+=1