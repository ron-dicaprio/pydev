# -*- coding:utf-8 -*-
import smtplib
import datetime
import time
from email.mime.text import MIMEText
#from email.mime.multipart import MIMEMultipart
#from email.mime.image import MIMEImage
def py_email(subject,message_con,to_user):
    to_user=[to_user]
    from_user = '1102346940@qq.com'
    from_passwd = 'password'
    mail_server = smtplib.SMTP('smtp.qq.com',25)
    mail_server.login(from_user,from_passwd)
    message = MIMEText(message_con, 'plain', 'utf-8')
    message['Subject'] = subject
    message['From'] = from_user
    message['To'] = ','.join(to_user)
    try:
        mail_server.sendmail(from_user, message['To'].split(','), message.as_string())
        print('email send success!')
    except Exception as e:
        print(e)
    mail_server.quit()
