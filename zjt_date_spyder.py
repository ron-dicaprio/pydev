# -*- coding: utf-8 -*-
#!/usr/bin/env python
#@author epoint_caitao
#单线程爬虫
import re
import requests
import time
import pymysql
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='Gepoint', db='pydb',charset='utf8mb4')
cur = conn.cursor()
#数据前清库
deletesql = "TRUNCATE TABLE pypro"
reCount = cur.execute(deletesql)
print('清除数据库成功！')
conn.commit()
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'} 
#数据量大，取部分前100页
for page in range(1,100):
    print(page)
    url = 'http://www.cszjw.net/sfloor?p=%s' % (page)
    response = requests.get(url,headers = header)
    response.encoding='utf-8'
    #findcon = re.findall(r'<td>(.*?)</td>'+'\n',response.text,re.S|re.M)
    #项目名称
    findtitle = re.findall(r'title="(.*?)">',response.text,re.S|re.M)
    #项目地址
    findaddr = re.findall(r'<td style="text-align:left">(.*?)</td>',response.text,re.S|re.M)
    #预售编号
    findnum = re.findall('\w{2}'+'\d{2}-\d{4}',response.text,re.S|re.M)
    #获证日期
    finddate = re.findall("\d{4}/\d{2}/\d{2}",response.text,re.S|re.M)
    #print('\n项目名称:\n',findtitle,'\n项目地址:\n',findaddr,'\n预售编号:\n',findnum,'\n获证日期:\n',finddate)
    time.sleep(1)
    #缓缓，住建厅的网站扛不住了
    for i in range(0,len(findtitle)):
        insertsql = "insert into pypro (proname,addr,date,num) values ('%s','%s','%s','%s')" % (findtitle[i],findaddr[i],finddate[i],findnum[i])
        reCount = cur.execute(insertsql)
        #print(insertsql)
        conn.commit()
    #print('项目名称为：',len(findtitle),findtitle,'\n项目地址为：',len(findaddr),findaddr)
conn.close()
