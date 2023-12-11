import requests
encoded_item="html parse in python"
r = requests.get("https://github.com/search?q=python+language%3A+parse&type=code", auth=('user', 'pass'))
print(r.status_code)
# 200
print(r.headers['content-type'])
# 'application/json; charset=utf8'
# r.encoding
# 'utf-8'
rtext=r.text
print(rtext)
# '{"type":"User"...'
print(r.json())
# {'private_gists': 419, 'total_private_repos': 77, ...}