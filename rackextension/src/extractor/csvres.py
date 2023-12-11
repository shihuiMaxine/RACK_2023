import re
import csv
import requests
import re
# import rack
# from rack.core.TokenStemmer import TokenStemmer
file1= open("example.txt", "r")
# url ="https://github.com/thesues/opensuse-topics/blob/6ac12b822a87abc8262753f2162594cdb02eba29/blog-upload.py"
# url ="https://github.com/Pinyto/cloud/blob/6f959308b121b398eabf3f536ead9ae90e4efdee/service/parsehtml.py"
url="https://github.com/certbot/certbot/blob/d8392bf39472216920e0b88c4d4e77ddbf4df5ab/acme/acme/client.py"
url = 'https://github.com/getsentry/sentry/blob/71be02dca325de7c709503ddccc4a020a65272bc/src/sentry/tasks/email.py'
# url="https://github.com/certbot/certbot/blob/d8392bf39472216920e0b88c4d4e77ddbf4df5ab/acme/acme/client.py"
# url = "https://github.com/search?%2Fcode%3F=&q=parse&type=code"
total1=[]
totalcontent=[]
header1=["website","codecontent","api"]
header2=["website","api"]
apidict={}
apidictorder={}
webcondict={}
with open('data_code.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header1)
    for j in file1:
        response = requests.get(j)
        # print(j)
        total1.append(j.rstrip("\n"))
        # Send an HTTP GET request to the URL
        # print(total1)
        url=j.rstrip("\n")
        # url="https://github.com/apache/airflow/blob/09880741cbfc4c1e6d433d1e7fac60deccd10a97/dev/send_email.py"
        response = requests.get(url)

            # Check if the request was successful (status code 200)
        if response.status_code == 200:
            text1=response.text
            # Print the content of the page (HTML source code)
            # print(response.text)
        
            rawline=text1.split("rawLines")[1]
            # print(rawline.split("stylingDirectives")[0])
            codecontent=rawline.split("stylingDirectives")[0]
            # print("hello world")
            # print(len(codecontent.split(",\"")))
            # print("hello world")
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
            # print((listwithoutcomments[len(listwithoutcomments)-1])[0:lengthlast-4])
            listwithoutcomments[0]=listwithoutcomments[0][4:len(listwithoutcomments)]
            listwithoutcomments[len(listwithoutcomments)-1]=(listwithoutcomments[len(listwithoutcomments)-1])[0:lengthlast-4]
            contentwithourcomments=""
            for i in listwithoutcomments:
                contentwithourcomments+=i+"\n"
            # print(i)
            totalcontent.append(contentwithourcomments)
            
            pattern = r"\w+\("
            method_names = re.findall(pattern, contentwithourcomments)
            list1=[]
            string1=""
            for name in method_names:
                nameele=name[0:len(name)-1]
                if nameele not in list1:
                    if nameele != "print":
                        list1.append(nameele)
                        string1+=nameele
                        string1+=" "
            # print(list1)
            webcondict[j]=contentwithourcomments
            data1=[j,contentwithourcomments,list1]
            writer.writerow(data1)
            k=['MIMEText', 'sendmail','SMTP','MIMEMultipart','login']

            k=["range", "gcd", "len", "int", "set"]
            # TokenStemmer().performStemming(a)
            numapi=0
            apisame=[]
            for i in k:
                if i in list1:
                    numapi+=1
                    apisame.append(i)
                    print(i)
            if numapi!=0:
                apidict[j]=apisame
        else:
            print("Failed to fetch the page. Status code:", response.status_code)
    # print(apidict)
    print(apidict.keys())
    for n in apidict.keys():
        print(len(apidict[n]))
    with open('data_codeapi.csv', 'w', encoding='UTF8') as f2:
        writer = csv.writer(f2)
        writer.writerow(header2)
        for i in range (0, len(k)):
            print(len(k)-i)
            for n in apidict.keys():
                if (len(apidict[n])==(len(k)-i)):
                    apidictorder[n.rstrip("\n")]=apidict[n]
                    # if n in webcondict.keys():
                    data2=[n.rstrip("\n"),apidict[n]]
                    writer.writerow(data2)
        print(apidictorder)

    
    with open("dataOutput.txt", "w") as filerf:
        filerf.writelines(totalcontent)


