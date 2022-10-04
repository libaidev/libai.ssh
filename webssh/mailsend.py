# -* - coding: UTF-8 -* -
# !/usr/bin/python3

import os
import sys
import time
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP_SSL

file_name = "lichuanyi.log.1662798085"
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
    "password": "",
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
