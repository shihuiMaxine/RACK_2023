import re
import csv
#?
file = open("website.csv")

print(type(file))
csvreader = csv.reader(file)
list1=[]
count1=0
cont=""
# print(csvreader.split("{"))
header = ['api name']

id=0
with open('api_2.csv', 'w', encoding='UTF8') as f:

    writer = csv.writer(f)

    # write the header
    writer.writerow(header)
    
    listapi=[]
    for row in csvreader:
        writer.writerow(csvreader.split("{"))