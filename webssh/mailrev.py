# -* - coding: UTF-8 -* -
# !/usr/bin/python3

from email.header import decode_header
from email.parser import Parser
import poplib

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
