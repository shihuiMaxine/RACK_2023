import requests
from bs4 import BeautifulSoup
import re
import csv
# developer_token = "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"
developer_token ="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"

def execute_github_call(call_url):
    developer_token ="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"

    response = ""
    try:
        # Adding the token
        headers = {"Authorization": f"token {developer_token}", "Content-Type": "application/html"}
        response = requests.get(call_url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        script_tags = soup.find_all("script", type="application/json")
        # print(response.content)
        for script_tag in script_tags:
            json_data = script_tag.string
            # You may want to further process the JSON data
            # print(json_data)
        # print(response.status_code)

        if response.status_code == 200:
            
            response_data = response.text

                
            return response_data
        
        else:
            print(f"Failed to collect the results from GitHub. Status code: {response.status_code}")
            response.raise_for_status()
        
    except requests.exceptions.RequestException as exc:
        print(f"Request failed: {exc}")
        return ""

if __name__ == "__main__":
    # call_url = "https://github.com/thesues/opensuse-topics/blob/6ac12b822a87abc8262753f2162594cdb02eba29/blog-upload.py"
    # call_url ="https://github.com/search?q=python+language%3A+parse+html&type=repositories"
    # reading csv files using pandas
    call_url ="https://api.github.com/search/code?q=reading+csv+files+using+pandas+in:file+language:python"
    # listinput= input()
    # call_url ="https://api.github.com/search/code?q=How+to+calculate+GCD+of+two+numbers+?+in:file+language:python"
    # call_url ="https://api.github.com/repos/redhat-performance/tuned/issues/events{/number}"
    # call_url = "https://github.com/huggingface/transformers/blob/bf7cfac20a08fa401d35d5a3d14246f4119d1f52/src/transformers/trainer.py#L2424"
    result = execute_github_call(call_url)
    htmlresult=result.split(",")
    
    # header=["code"]
    # with open('website.csv', 'w', encoding='UTF8') as f:

    #     writer = csv.writer(f)
    #     writer.writerow(header)
    #     data1=[response_data]
    #     writer.writerow(data1)
    file_path = 'example.txt'

    # Writing the content to the text file
    file1=""
    with open(file_path, 'w') as file:
        for i in htmlresult:
            if "html_url" in i:
                if ".py" in i:
                    print("html_url:")
                    print(i[12:len(i)-1])
                    file1+=i[12:len(i)-1]+"\n"
        file.write(file1)

    # for i in  result.split("\n"):
    #     if "payload" in i:
    #         print(i)

