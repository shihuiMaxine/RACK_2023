import re
import csv
file = open("data_code.csv")

print(type(file))
csvreader = csv.reader(file)
total1=[]
# for row in csvreader:
#     # total1.append(row[1])
#     print(row[1])
# print(total1[0])
# code= csvreader[1][1]
# print(csvreader[1])
# pattern = r"\w+\("
header1=["website","codecontent","api"]
# method_names = re.findall(pattern, code)
# list1=[]
# string1=""
# for name in method_names:
#     nameele=name[0:len(name)-1]
#     if nameele not in list1:
#         if nameele != "print":
#             list1.append(nameele)
#             string1+=nameele
#             string1+=" "
# print(list1)
# with open('data_api.csv', 'w', encoding='UTF8') as f:
#     writer = csv.writer(f)
#     for row in csvreader:
#         website1=row[0]
#         content1=row[1]


#     # write the header
#     writer.writerow(header1)
print(csvreader)
file2= open("dataOutput.txt", "r")
total2=[]
for i in file2:
    total2.append(i)
# print(len(total2))
line_number = 8

file_name="data_code.csv"

try:
    with open(file_name, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        
        for current_line_number, row in enumerate(csv_reader, start=1):
            if current_line_number == line_number:
                print(f'Line {line_number}: {row}')
                break
            # print(current_line_number)
except FileNotFoundError:
    print(f'Error: File "{file_name}" not found.')
except Exception as e:
    print(f'An error occurred: {e}')