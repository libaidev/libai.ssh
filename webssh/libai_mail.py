# -* - coding: UTF-8 -* -
# !/usr/bin/python3

import os
import poplib
import sys
import time
from email.header import Header, decode_header
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.parser import Parser
from smtplib import SMTP_SSL

file_name = "openstack.log"
if len(sys.argv) > 1:
    file_name = str(sys.argv[1])

# maildir = os.path.join(os.getcwd(), "static\log")
maildir = "d:/opslog"
data_file = os.path.join(maildir, file_name)
with open(data_file, "r", encoding="utf-8", errors="ignore") as f:
    file_data = f.read()
now = time.strftime("%Y%m%d%H%M%S")
mail_info = {
    "from": "libaidev@aliyun.com",
    "to": "libaidev@aliyun.com",
    "host": "smtp.aliyun.com",
    "username": "libaidev@aliyun.com",
    "password": "buyongLi123",
    "subject": file_name + now,
    "text": file_data,
    "encoding": "utf-8"
}
smtp = SMTP_SSL(mail_info["host"])
smtp.ehlo(mail_info["host"])
smtp.login(mail_info["username"], mail_info["password"])
mail = MIMEMultipart()

txt = MIMEText(mail_info["text"], "plain", mail_info["encoding"])
mail.attach(txt)
mail["Subject"] = Header(mail_info["subject"], mail_info["encoding"])
mail["from"] = mail_info["from"]
mail["to"] = mail_info["to"]

app = MIMEApplication(open(data_file, "rb").read())
app.add_header("Content-Disposition", "attachment", filename=file_name)
mail.attach(app)

smtp.sendmail(mail_info["from"], mail_info["to"], mail.as_string())
smtp.quit()



email = 'libaidev@aliyun.com'
password = ''
pop3_server = 'pop3.aliyun.com'

server = poplib.POP3_SSL(pop3_server)
server.user(email)
server.pass_(password)
mail_total, total_size = server.stat()
print('message: %s.Size:%s' % (mail_total, total_size))
# list()返回所有邮件的编号:
resp, mails, octets = server.list()
# 获取最新一封邮件, 注意索引号从1开始:
index = len(server.list()[1])
for i in range(1, index):
    resp, lines, octets = server.retr(i)
    msg_content = b'\r\n'.join(lines).decode('utf-8')
    msg = Parser().parsestr(msg_content)
    print("Form: {}".format(msg.get('From')))
    print("To: {}".format(msg.get('To')))
    value, charset = decode_header(msg.get('Subject'))[0]
    print("Subject: {}".format(value.decode(charset)))
    parts = msg.get_payload()
    for part in parts:
        content_disposition = part.get_content_disposition()
        attachment_name = part.get_filename()
        content = part.get_payload(decode=True)
        if content_disposition == 'attachment':
            with open(attachment_name, 'wb') as f:
                f.write(content)
# server.dele(index)
server.quit()
