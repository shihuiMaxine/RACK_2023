import re
f = open("examplecode.txt", "r")
code = f.read()
# print(code)
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
print(list1)
file_name = 'output.txt'
with open(file_name, 'w') as txt_file:
    txt_file.writelines(list1)