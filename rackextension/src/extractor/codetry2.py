import re

def find_code_with_keyword(text, keyword):
    pattern = re.compile(r'\bdef\b.*?\b' + re.escape(keyword) + r'\b.*?(?=\bdef\b|$)', re.DOTALL)
    match = pattern.search(text)
    if match:
        return match.group(0)
    else:
        return None

# Your example code
code_text = """

def send_email(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    sendmail(msg)
    
def sendmail(msg):
    smtp = SMTP('smtp.example.com')
    smtp.login('username', 'password')
    smtp.sendmail('from@example.com', 'to@example.com', msg.as_string())

def compose_email(subject, body, attachment):
    msg = MIMEMultipart()
    msg.attach(MIMEText(body))
    msg['Subject'] = subject
    msg.attach(attachment)
    sendmail(msg)
    
def send_email2(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    sendmail(msg)
"""

# Keyword to search for
keyword = 'MIMEMultipart'

# Find code snippet containing the keyword
result = find_code_with_keyword(code_text, keyword)

if result:
    print(result)
else:
    print("Keyword not found in any code snippet.")
