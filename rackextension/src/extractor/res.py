import requests
import re
# url ="https://github.com/thesues/opensuse-topics/blob/6ac12b822a87abc8262753f2162594cdb02eba29/blog-upload.py"
# url ="https://github.com/Pinyto/cloud/blob/6f959308b121b398eabf3f536ead9ae90e4efdee/service/parsehtml.py"
url="https://github.com/certbot/certbot/blob/d8392bf39472216920e0b88c4d4e77ddbf4df5ab/acme/acme/client.py"
url = 'https://github.com/getsentry/sentry/blob/71be02dca325de7c709503ddccc4a020a65272bc/src/sentry/tasks/email.py'
# url="https://github.com/certbot/certbot/blob/d8392bf39472216920e0b88c4d4e77ddbf4df5ab/acme/acme/client.py"
# url = "https://github.com/search?%2Fcode%3F=&q=parse&type=code"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    text1=response.text
    # Print the content of the page (HTML source code)
    # print(response.text)
else:
    print("Failed to fetch the page. Status code:", response.status_code)
rawline=text1.split("rawLines")[1]
# print(rawline.split("stylingDirectives")[0])
codecontent=rawline.split("stylingDirectives")[0]
print("hello world")
print(len(codecontent.split(",\"")))
print("hello world")
file_path = 'examplecode.txt'
file1=""
pattern = r'#.*$'
pattern2 =r'\\"\\"\\"'
# print(len(codecontent.split(",")))
listwithoutcomments = []
lencomment2 = 0
for i in codecontent.split("\",\""):

    comment = re.findall(pattern, i)
    comment2 = re.findall(pattern2, i)
    if (comment != []):
        a=0

        # print(comment)
    else:
        # if (comment2 != []):
        if (len(comment2)==2):
            lencomment2 = 2
        if (len(comment2)==1):
            lencomment2 += 1
                
        if lencomment2 == 0:
            listwithoutcomments.append(i)
        # else:
        #     print(i)
        if lencomment2 == 2:
            lencomment2 =0
lengthlast=len(listwithoutcomments[len(listwithoutcomments)-1])
print((listwithoutcomments[len(listwithoutcomments)-1])[0:lengthlast-4])
listwithoutcomments[0]=listwithoutcomments[0][4:len(listwithoutcomments)]
listwithoutcomments[len(listwithoutcomments)-1]=(listwithoutcomments[len(listwithoutcomments)-1])[0:lengthlast-4]
contentwithourcomments=""
for i in listwithoutcomments:
    contentwithourcomments+=i+"\n"
    print(i)
# print(contentwithourcomments[1])
with open(file_path, 'w') as file:
    # for i in htmlresult:
    #     if "html_url" in i:
    #         if ".py" in i:
    #             print("html_url:")
    #             print(i[12:len(i)-1])
    #             file1=i[12:len(i)-1]+"\n"
    file.write(contentwithourcomments)
# for i in text1.split("rawLines"):
#     if "rawLines" in i:
#         print(i)
