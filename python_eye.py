# -*- coding:utf-8 -*-
#!/usr/bin/env python
import time
import os
import datetime
import pylog
'''
#pylog自定义日志类
#pylog detail code
import os
import datetime
if os.path.exists('logs'):
    pass
else:
    os.mkdir('logs')
#another kind of time format 
#datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def info(self):
    file = open('logs/%s.wrapper' % (datetime.datetime.now().date()),'a+',encoding='utf-8')
    file.writelines('###  %s |info| %s\n' % (datetime.datetime.now(),str(self)))
    file.close()
    
def warnnig(self):
    file = open('logs/%s.wrapper' % (datetime.datetime.now().date()),'a+',encoding='utf-8')
    file.writelines('###  %s |warn| %s\n' % (datetime.datetime.now(),str(self)))
    file.close()
    
def error(self):
    file = open('logs/%s.wrapper' % (datetime.datetime.now().date()),'a+',encoding='utf-8')
    file.writelines('###  %s |erro| %s\n' % (datetime.datetime.now(),str(self)))
    file.close()
'''
file_pwd = 'D:/software/apache-tomcat-7.0.85_64/webapps/sysinfo'
#路径是否存在
if os.path.isdir(file_pwd):
    print('path %s exist!' % (file_pwd))
    pylog.info(file_pwd,'exist')
else:
    os.makedirs(file_pwd)
#文件是否存在
if os.path.exists(file_pwd+'index.html'):
    pass
else:
    try:
        os.system('type nul > %s/index.html' % (file_pwd))
        print('index')
        pylog.info('index')
    except Exception as e:
        print('error!',e)
        pylog.error(e)
    
        
process_mysql = os.popen('tasklist | findstr mysql').readlines()
if len(process_mysql) == 0:
    try:
        os.system('net start mysql')
        pylog.info('mysql')
    except Exception as e:
        pylog.info('error',e)
else:
    pylog.info('tomcat')
#
process_tomcat = os.popen('tasklist | findstr wrapper.exe').readlines()
if len(process_tomcat) == 0:
    os.system('net start epointtomcat')
    pylog.info('net start epointtomcat')
    print('tomcat')
else:
    print('tomcat')
    pylog.info('tomcat')
    
import smtplib
from email.mime.text import MIMEText
#from email.mime.multipart import MIMEMultipart
#from email.mime.image import MIMEImage
from_user = '1102346940@qq.com'
from_passwd = '@password'
to_user = ["love6018@hotmail.com","1102346940@qq.com"]
file = open('logs/%s.wrapper' % (datetime.datetime.now().date()),'r+',encoding='utf-8')
message_text = file.read()
print(message_text)
mail_server = smtplib.SMTP('smtp.qq.com',25)
mail_server.login(from_user,from_passwd)
message = MIMEText(message_text, 'plain', 'utf-8')
message['Subject'] = 'tomcat'
message['From'] = from_user
message['To'] = ','.join(to_user)
while True:
    if datetime.datetime.now().hour > 1:
        mail_server.sendmail(from_user, message['To'].split(','), message.as_string())
        print('1')
        pylog.info('2')
        break
    else:
        print('3')
        time.sleep(3600)
print('email send success!')
mail_server.quit()
