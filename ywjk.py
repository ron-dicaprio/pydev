# -*- coding:utf-8 -*-
# !/usr/bin/env python
import requests
import py_email
#http://192.168.123.88:8091/运维监控平台地址
webservice_url = ['http://192.168.123.88:8091/']
for i in range(0, len(webservice_url)):
    try:
        response = requests.get(webservice_url[i])
        print(response.status_code)
        if response.status_code == 200:
            print(webservice_url[i]+'接口访问正常！')
        else:
            print(webservice_url[i]+'接口访问异常！')
           #status_code不为200时，发送邮件通知相关人员
            py_email.py_email('接口访问异常！', '%s\n接口访问异常！' % (webservice_url[i]), r'C:\Users\sysadmin\Pictures\1.png', '1102346940@qq.com')
    except Exception as e:
        #请求报错的时候也发邮件通知相关人员
        print(e)
        py_email.py_email('接口访问异常！', '%s\n接口访问异常！错误信息为：%s' % (webservice_url[i], e), r'C:\Users\sysadmin\Pictures\1.png', '1102346940@qq.com')
