# -*- coding: utf-8 -*-
#!/usr/bin/env python
#@author epoint_caitao
#from bs4 import BeautifulSoup as soup
import re
import requests
#import pymysql
#conn = pymysql.connect(host='127.0.0.1', user='root', passwd='Gepoint', db='pydb',charset='utf8mb4')
#cur = conn.cursor()
chorme_header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv 11.0) like Gecko'} 
url = 'https://oa.epoint.com.cn/EpointTrainingManage/TrainingFile/File/'
response = requests.get(url,headers = chorme_header)
response.encoding='utf-8'
target = re.findall(r'A HREF="(.*?)"',response.text)
file_no = 0
for i in range(1,len(target)):
    url1 = 'https://oa.epoint.com.cn' + target[i]
    response1 = requests.get(url1,headers = chorme_header)
    response1.enoding ='utf-8'
    target1 = re.findall(r'<A HREF="(.*?)">',response1.text)
    url2 = 'https://oa.epoint.com.cn' + target1[1]
    print('url2:',url2)
    #strsql = "insert into pyurl set pyepurl = '%s'" % (url2)
    #cur.execute(strsql)
    #conn.commit()
    response2 =requests.get(url2,headers = chorme_header)
    file_no += 1
    with open('E:\\pydownload\\%s.%s' % (file_no,target1[1].split('.')[-1]),'wb+') as file:
        file.write(response2.content)
        print(i,'file saved,url is ',url2)
        file.close()
#conn.close()
