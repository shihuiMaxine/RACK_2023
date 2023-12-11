import re

def remove_comments(input_code):
    lines = input_code.split('\n')
    new_lines = []

    in_comment_block = False

    for line in lines:
        line = line.strip()

        if not in_comment_block:
            if line.startswith("#"):
                new_lines.append(line)
            elif '"""' in line or "'''" in line:
                in_comment_block = True
                new_lines.append(line[:line.find('"""')] if '"""' in line else line[:line.find("'''")])
            else:
                new_lines.append(re.sub(r"#.*", "", line))
        else:
            if '"""' in line or "'''" in line:
                in_comment_block = False
                new_lines.append(line[line.find('"""')+3:] if '"""' in line else line[line.find("'''")+3:])
            else:
                new_lines.append("")

    return '\n'.join(new_lines)

# Your example code
code = '''
# file parsing to get some values :
spaces = re.compile("[ \t]+|\n")

IP_PROTOS={}
try:
    f=open("/etc/protocols")
    for l in f:
        try:
            if l[0] in ["#","\n"]:
                continue
            lt = tuple(re.split(spaces, l))
            if len(lt) < 3:
                continue
            IP_PROTOS.update({lt[2]:int(lt[1])})
        except:
            log_loading.info("Couldn't parse one line from protocols file (" + l + ")")
    f.close()
except IOError:
    log_loading.info("Can't open protocols file")
'''

new_code = remove_comments(code)
print(new_code)

