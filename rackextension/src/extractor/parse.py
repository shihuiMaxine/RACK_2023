from bs4 import BeautifulSoup
from rack.config import StaticData
import requests, csv
from rack.similarity.MyTokenizer import MyTokenizer
from rack.core. CodeTokenProvider import CodeTokenProvider
# ?
# Open a file in read-only mode
file = open('qlink1.txt', 'r')
header = ['title','answer_code']
# Read the contents of the file
contents = file.readlines()

# Print the contents of the file
print(contents)
count=0
with open('answer2.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    for i in contents:


# for i in contents:
    # print(i)
        # print(1)
        count+=1
        if count%2 == 1:
            print(i)
            title1=i
        else:
            print(i)
    #


            # Send a GET request to the URL
            url = i.strip()
            response = requests.get(url)

            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find all code elements in the HTML and concatenate their text content
            code_content = ""
            code_elements = soup.find_all('code')
            for code_element in code_elements:
                code_content += code_element.get_text() + "\n"

            # Print the concatenated code content
            print(code_content)
            data1 = [title1,code_content]
            # print(data1)
            writer.writerow(data1)
file.close()