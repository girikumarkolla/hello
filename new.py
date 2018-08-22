import re


import smtplib

#subjuct import module
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#attachment import module
from email.mime.base import MIMEBase
from email import encoders

import re
a = []
bob = open("giri.txt","r")
#bob.read()
pattern = r"[a-zA-Z0-9_.]+@[a-zA-Z.]+"
matches = re.findall(pattern, bob.read())
for match in matches:
        #print(match,end =" ")
        a.append(match)
print(a)
bob.close()



#subject starts
email_user = 'subrainstesting@gmail.com'
text = 'Python!'
subject = 'python'
for email_send in a:
        #print(email_send)
        #email_send = email_send
        msg = MIMEMultipart()
        msg['From'] = email_user
        msg['To'] = email_send
        msg['subject'] = subject
        body = "hello sir"
        msg.attach(MIMEText(body,'plain'))
        # attachment starts
        filename = "email_attachment.py"
        attachment = open(filename, 'rb')
        part = MIMEBase("application","octet-stream")
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header("content-Disposition","attachment:filename = " +filename)
        msg.attach(part)
        # attachment ends
        text = msg.as_string()
        #subject ends
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        # login
        server.login(email_user,'SuBrains@123')
        #sending mail
        server.sendmail(email_user,email_send,text)

server.close()

