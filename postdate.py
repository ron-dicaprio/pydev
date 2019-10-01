# -*- coding:utf-8 -*-
import requests
url1 = '1'
url2 = '2'
log_auth = {
    "txtUserName":'admin',
    "txtPwd":'admin',
    }
chorme_header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2652.2 Safari/537.36'}
response = requests.post(url1,data = log_auth,headers = chorme_header) #,json=True
cookie1 = response.cookies.get_dict()
print(cookie1)
response.encoding = 'utf -8'
response2 = requests.get(url2,cookies=cookie1,headers = chorme_header)
print(response2.text)

