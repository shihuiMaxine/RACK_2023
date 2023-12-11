# import rack
# from rack import main
# # query = input()
# import sys

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
# import src.extractor.GitHubClient
# print (sys.argv)
totalcont=[]
lista=[]
# dicta=[]
dicta={}

print (sys.argv[2:])
stringquery=' '.join(sys.argv[2:])
print(stringquery)

# print("hello")
# query = "send email"
# stringquery="Accessing a list of rows from mySQL table"
question="https://api.github.com/search/code?q="
listquery=stringquery.split(" ")
for i in range (0, len(listquery)):
    # if i != (len(stringquery)-1):
    question+=listquery[i] + "+"
    # else:
        # question+=i
question += "in:file+language:python"

call_url ="https://api.github.com/search/code?q=Accessing+a+list+of+rows+from+mySQL+table+in:file+language:python"
result = extractor.GitHubClient.execute_github_call(call_url)
htmlresult=result.split(",")
listgit=[]
for i in htmlresult:
    if "html_url" in i:
        if ".py" in i:
            # print("html_url:")
            # print(i[12:len(i)-1])
            listgit.append(i[12:len(i)-1])
            
# extractor.GitHubClient.execute_github_call(call_url)
            # extractor.getcodeapi.github_url_to_raw_url(i[12:len(i)-1])
apitoken=main.main(stringquery)
print(apitoken)

# /Users/gaoshihui/Desktop/whltest10/rackextension/src/rack1.py
# Accessing a list of rows from mySQL table

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
        # print(raw_url)
        if response.status_code == 200:

            return github_url,raw_url
        else:
            return "",""
# for i in listgit:
#     github_url,raw_url = github_url_to_raw_url(i)
#     print(github_url)
#     print(raw_url)

giturllist=[]
totalraw=[]
n=0
for i in listgit:
    # if n==0:
    github_url = i

    # Convert to raw URL
    giturl,raw_url = github_url_to_raw_url(github_url)
    if giturl != "":
        totalraw.append(raw_url)
        giturllist.append(giturl)

        # Print the raw URL
        # print(raw_url)
    # n+=1
# k=["execute", "len", "cursor", "append", "range"]
k=apitoken
def remove_comments(input_code):
    # Use a regular expression to match and remove comments
    cleaned_code = re.sub(r'^\s*#.*|(""")[\s\S]*?\1|(\'\'\')[\s\S]*?\2', '', input_code)
    return cleaned_code
def find_code_snippet(code_text, target_content):
    # print(code_text)
    # code_without_comments = remove_comments_from_code(code_text)
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
    k=apitoken
    # k=['MIMEText', 'sendmail','SMTP','MIMEMultipart','login']
    # k=['hexdigest', 'md5', 'encode', 'update', 'hashlib']
    # k=["range", "gcd", "len", "int", "set"]
    # k=["execute", "len", "cursor", "append", "range"]

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
            # print(f"Output {m}:\n{snippet}\n{'='*40}")
            if m not in apicontent:
                apicontent.append(m)
            # print(apicontent)
            codecontent.append(f"{snippet}\n{'='*40}")
            # codecontent.append(f"Output {m}:\n{snippet}\n{'='*40}")
    # print("hello")
    # print(codecontent[0])
    # print("hello")
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
listrtotal=[]
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
        # print(len(listr[3]))
        for z in listr[3]:
            # u=0
            print(z)
            listrtotal.append(z)



    co +=1
       

# print( type(github_url_to_raw_url(listgit[i])))
# print(github_url_to_raw_url(i))
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

    # print(countapi)
    # print(list1)
    list1tital.append(listsame)
    listtotalcode.append(i)
for i in range (0, len(list1tital)-1):
    print(listtotalcode[i])
    print(list1tital[i])
    clean_code = remove_comments(listtotalcode[i])
    codedict[clean_code]=len(list1tital[i])
    
    # codedict[len(list1tital[i])]= listtotalcode[i]
    # print("\n")
# print( type(github_url_to_raw_url(listgit[i])))
# print(github_url_to_raw_url(i))
# print(codedict)
# my_dict = {'banana': 3, 'apple': 1, 'orange': 4, 'kiwi': 2}
# sorted_dict_keys = dict(sorted(my_dict.items()))
# print(sorted_dict_keys)

# sorted_dict_keys = dict(sorted(codedict.items()))
# print(sorted_dict_keys)

# for i in range (0, len(sorted_dict_keys.keys())-1):

# my_dict = {'banana': 3, 'apple': 1, 'orange': 4, 'kiwi': 2}

# sorted_dict_descending = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

# print(sorted_dict_descending)


sorted_dict_descending = dict(sorted(codedict.items(), key=lambda item: item[1], reverse=True))
# print(list(sorted_dict_descending.keys()))
cn=0
for i in list(sorted_dict_descending.keys()):
    if cn < 3:
        print(i)
        print(sorted_dict_descending[i])
        

    cn+=1

# for i in range (0, len(sorted_dict_descending.keys())-1):
#     if i <3:
#         print(sorted_dict_descending.keys()[i])

        # print(sorted_dict_descending[sorted_dict_descending.keys()[i]])



