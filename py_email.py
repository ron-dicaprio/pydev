# -*- coding:utf-8 -*-
# !/usr/bin env python
import smtplib
import datetime
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
#from email.mime.image import MIMEImage
def py_email(subject,message_con,filepaths,to_user):
    to_user=[to_user]
    from_user = '1102346940@qq.com'
    from_passwd = 'nshfzkkyjspebaac'
    mail_server = smtplib.SMTP('smtp.qq.com',25)
    mail_server.login(from_user,from_passwd)
    filepaths = filepaths.replace('/','\\')
    print(filepaths)
    #message = MIMEText(message_con, 'plain', 'utf-8')
    #message = MIMEMultipart()
    #构建一个带附件的实例
    message = MIMEMultipart()
    message['Subject'] = subject
    message['From'] = from_user
    message['To'] = ','.join(to_user)
    message.attach(MIMEText(message_con, 'plain', 'utf-8'))
    for filenames in (filepaths.split(';')):
        print(filenames)
        attachfile =  MIMEText(open(filenames, 'rb').read(), 'base64', 'utf-8')
        attachfile["Content-Type"] = 'application/octet-stream'
        attachfile["Content-Disposition"] = 'attachment; filename=%s' % (str(filenames).split('\\')[-1])
        message.attach(attachfile)
    try:
        mail_server.sendmail(from_user, message['To'].split(';'), message.as_string())
        print('email send success!')
    except Exception as e:
        print(e)
    mail_server.quit()
