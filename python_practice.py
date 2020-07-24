# -*- coding: utf-8 -*-
#!/usr/bin/env python
#爬取新点的文件服务器并且下载到本地，后期可跟数据库做关联。
#from  bs4 import BeautifulSoup as soup
import re
import requests
import pymysql
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='Gepoint', db='pydb',charset='utf8mb4')
cur = conn.cursor()
chorme_header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2652.2 Safari/537.36'} 
url = 'https://oa.epoint.com.cn/EpointTrainingManage/TrainingFile/File/'
response = requests.get(url,headers = chorme_header)
response.encoding='utf-8'
target = re.findall(r'A HREF="(.*?)"',response.text)
#file_no = 0
#len(target)
for i in range(1,5):
    url1 = 'https://oa.epoint.com.cn' + target[i]
    response1 = requests.get(url1,headers = chorme_header)
    response1.enoding ='utf-8'
    target1 = re.findall(r'<A HREF="(.*?)">',response1.text)
    url2 = 'https://oa.epoint.com.cn' + target1[1]
    print('url2:',url2)
    strsql = "insert into pyurl set pyepurl = '%s'" % (url2)
    cur.execute(strsql)
    conn.commit()
    '''
    response2 =requests.get(url2,headers = chorme_header)
    file_no += 1
    with open('E:\\pydownload\\%s.%s' % (file_no,target1[1].split('.')[-1]),'wb+') as file:
        file.write(response2.content)
        print(i,'file saved,url is ',url2)
        file.close()
'''
conn.close()
'''
# -*- coding: utf-8 -*-
#!/usr/bin/env python
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
#数据量大，取部分页面
for page in range(300,594):
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
    time.sleep(0.5)
    #缓缓，住建厅的网站扛不住了
  
    for i in range(0,len(findtitle)):
        insertsql = "insert into pypro (proname,addr,date,num) values ('%s','%s','%s','%s')" % (findtitle[i],findaddr[i],finddate[i],findnum[i])
        reCount = cur.execute(insertsql)
        #print(insertsql)
        conn.commit()
    #print('项目名称为：',len(findtitle),findtitle,'\n项目地址为：',len(findaddr),findaddr)
    
conn.close()


import pygame
import sys
import os
import datetime
import math
import random
from pygame.locals import *
pygame.init() #初始化
scr = pygame.display.set_mode((1024,461),0,32)
pygame.display.set_caption('植物大战僵尸')
BG_Pic = pygame.image.load(r"d:\\spy\\ZB01.jpg").convert()
player = pygame.image.load(r"d:\\spy\\pla.jpg").convert_alpha()
while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        pygame.quit()
        exit()
    scr.blit(BG_Pic,(0,0))
    x,y = pygame.mouse.get_pos()  #获取鼠标位置
    x = x - player.get_width() / 2
    y = y - player.get_height() / 2
    scr.blit(player,(x,y))
    pygame.display.update()
pygame.quit()





# -*- coding: utf-8 -*-
#!/usr/bin/env python
#soup与re的配合使用
import re
import requests
from bs4 import BeautifulSoup as soup
#import pymysql
#conn = pymysql.connect(host='127.0.0.1', user='root', passwd='Gepoint', db='pydb',charset='utf8mb4')
#cur = conn.cursor()
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'} 
#数据量大，取部分页面
url = 'http://www.cszjw.net/floorinfo/201710250039'
response = requests.get(url,headers = header)
response.encoding='utf-8'
spyall = soup(response.text,'lxml').find_all('div',class_="hs_table")
spyall = str(spyall)
spyspec = re.findall(r'<td>(.*?)</td>',spyall,re.S|re.M)
print('本次一共查询到',len(spyspec),'条数据')

for i in range(0,len(spyspec)//8):
    n = i * 8
    insertsql = "insert into pydetail (salesno,buildinfo,salesdate,landsquar,landno,designno,uselandno,buildlandno) values ('%s','%s','%s','%s','%s','%s','%s','%s')" % (spyspec[n],spyspec[n+1],spyspec[n+2],spyspec[n+3],spyspec[n+4],spyspec[n+5],spyspec[n+6],spyspec[n+7])
    print(insertsql)
#    reCount = cur.execute(insertsql)
#    conn.commit()
#conn.close()

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
#数据量大，取部分页面
url = 'http://www.cszjw.net/floorinfo/201710250039'
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
time.sleep(0.5)
    #缓缓，住建厅的网站扛不住了
    

        conn.commit()
    #print('项目名称为：',len(findtitle),findtitle,'\n项目地址为：',len(findaddr),findaddr)

conn.close()
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
#数据量大，取部分页面
for page in range(254,590):
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
    time.sleep(0.5)
    #缓缓，住建厅的网站扛不住了
    
    for i in range(0,len(findtitle)):
        insertsql = "insert into pypro (proname,addr,date,num) values ('%s','%s','%s','%s')" % (findtitle[i],findaddr[i],finddate[i],findnum[i])
        reCount = cur.execute(insertsql)
        #print(insertsql)
        conn.commit()
    #print('项目名称为：',len(findtitle),findtitle,'\n项目地址为：',len(findaddr),findaddr)

conn.close()
#337

import re
import requests
import pymysql
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='Gepoint', db='pydb',charset='utf8mb4')
cur = conn.cursor() 
#数据前清库
deletesql = "TRUNCATE TABLE pypro"
reCount = cur.execute(deletesql)

#更新unt = cur.execute(deletesql)
print('清除数据库成功！')
conn.commit()

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'} 
#数据量大，取部分页面
for page in range(1,2):
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
    print('\n项目名称:\n',findtitle,'\n项目地址:\n',findaddr,'\n预售编号:\n',findnum,'\n获证日期:\n',finddate)
    
    for i in range(0,len(findtitle)):
        insertsql = "insert into pypro (proname,addr,date,num) values ('%s','%s','%s','%s')" % (findtitle[i],findaddr[i],finddate[i],findnum[i])
        reCount = cur.execute(insertsql)
        print(insertsql)
        conn.commit()
    #print('项目名称为：',len(findtitle),findtitle,'\n项目地址为：',len(findaddr),findaddr)
    
conn.close()

#爬取开盘信息结果存入数据库
import re
import requests
import pymysql
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='Gepoint', db='pydb',charset='utf8mb4')
cur = conn.cursor()
#数据前清库
deletesql = "TRUNCATE TABLE pypro"
reCount = cur.execute(deletesql)

#更新unt = cur.execute(deletesql)
print('清除数据库成功！')
conn.commit()

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'} 
#数据量大，取前四页
for page in range(1,2):
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
    print('\n项目名称:\n',findtitle,'\n项目地址:\n',findaddr,'\n预售编号:\n',findnum,'\n获证日期:\n',finddate)
 
    for i in range(0,len(findtitle)):
        insertsql = "insert into pypro (proname,addr,date,num) values ('%s','%s','%s','%s')" % (findtitle[i],findaddr[i],finddate[i],findnum[i])
        reCount = cur.execute(insertsql)
        print(insertsql)
        conn.commit()
    #print('项目名称为：',len(findtitle),findtitle,'\n项目地址为：',len(findaddr),findaddr)
 
conn.close()



#mysql相关引用及配置
import pymysql
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='Gepoint', db='pydb',charset='utf8')
cur = conn.cursor()
#爬虫相关引用及配置
import re
import requests
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'} 
no = 1
for i in range(1,590):
    url = 'http://www.cszjw.net/sfloor?p=%s' % (i)
    response = requests.get(url,headers = header)
    response.encoding='utf-8'
    #findcon = re.findall(r'<td>(.*?)</td>'+'\n',response.text,re.S|re.M)
    #匹配title
    findcon = re.findall(r'title="(.*?)">',response.text,re.S|re.M)
#    findcon = str(findcon).split(',')  len(findcon)
    for n in range(1,len(findcon)):
        sql = "insert into pypro (proname,no) values ('%s','%s')" % (findcon[n],no)
        no += 1
        print('执行的sql为：\n',sql)
        reCount = cur.execute(sql)
        print('sql执行受影响的行数为:\n',reCount)
        #print('查询结果为:\n',cur.fetchall())
        #触发commit事件，插入数据库
        conn.commit()
    #print(findcon)
    #sql = 'insert into pydate (name) values (%s)' % (findcon)
    #print()

#reCount = cur.execute(sql)
#print(cur.fetchall())
conn.close()



import requests
import re
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'}
for i in range(1,2):
    url = 'http://www.cszjw.net/sfloor?p=%s' % (i)
    response = requests.get(url,headers = header)
    response.encoding='utf-8'
    #findcon = re.findall(r'<td>(.*?)</td>'+'\n',response.text,re.S|re.M)
    #匹配title
    findcon = re.findall(r'title="(.*?)">',response.text,re.S|re.M)
    print(findcon)
    sql = 'insert into pydate (name) values (%s)' % (findcon)
    reCount = cur.execute(sql)
    print()
conn.close()



import pymysql
import requests
import re
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'}
for i in range(1,590):
    url = 'http://www.cszjw.net/sfloor?p=%s' % (i)
    response = requests.get(url,headers = header)
    response.encoding='utf-8'
#    findcon = re.findall(r'<td>(.*?)</td>'+'\n',response.text,re.S|re.M)
    #匹配title
    findcon = re.findall(r'title="(.*?)">',response.text,re.S|re.M)
    print(findcon)

import pymysql
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='Gepoint', db='inteligentsearch',charset='utf8')
cur = conn.cursor()

#MySQL查询
sql = "select * from frame_user"
reCount = cur.execute(sql)  # 执行并返回受影响的行数
data = cur.fetchall()       # 返回查询结果
print('受影响行数为：\n',reCount,'\n返回结果为:\n',data)

[^>]*  re正则的匹配

http://www.cszjw.net/sfloor?p=100000
for i in range(1,10000):
import requests
from bs4 import BeautifulSoup as soup
url = 'http://szjw.changsha.gov.cn/zwgk/tzgg/lslp/'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'}
response = requests.get(url,headers = header)
response.encoding='utf-8'
print(response.text)


import requests
count = 0
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
file = open('d:\\spy\\gld_url_wash_1.txt','r+',encoding = 'utf-8')
for url in file.readlines():
    count += 1
    response = requests.get(url,headers = header)
    response.encoding='utf-8'
    print(url,'\n',response.text)
file.close()


import requests
count = 0
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
file = open('d:\\spy\\gld_url_wash_1.txt','r+',encoding = 'utf-8')
n = 0
for url in file.readlines():
    n += 1
    print(url)
    response = requests.get(url,headers = header)
    response.encoding='utf-8'
    print(response.text,'\n')
    if n == 2:
        break
    else:pass
file.close()



import requests
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
file = open("d:\\spy\\gld_url_wash_1.txt",'r+')
n = 0
for i in file.readlines():
    response = requests.get(i,headers = header)
    response.encoding='utf-8' 
    n += 1
    print(i)
    print(response.text)
    if  n == 2:
        break
    else:pass

from bs4 import BeautifulSoup as soup
import requests
import re
import os
#print('默认编码格式为:',sys.getdefaultencoding())
#agent:Chrome
#取url数据
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
file  = open('d:\\spy\\gld_url_wash_1.txt','r+')
for url in file.readlines():
    response = requests.get(url,headers = header)
    #contenct = soup.find_all(self, name, attrs, recursive, text, limit)


from bs4 import BeautifulSoup as soup
import requests
import re
import os
#print('默认编码格式为:',sys.getdefaultencoding())
#agent:Chrome
#取数据
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
#while True:
    #url = input('请输入网址\n>>>')
for i in range(1,992):
    url=('http://hnsggzy.com/scztfr/index_%s.jhtml' % (i))
    if i == 1:
        url = 'http://hnsggzy.com/scztfr/index.jhtml'
    else:
        pass
    #print(url)
#try:
    response = requests.get(url,headers = header)
    #if response.status_code == 200:
    #    pass
    #else:
    #    print('输入网址不合法，请重新输入')
    response.encoding='utf-8' #强行转码
    #爬取内容<div class="article-list3-t">
    con = soup(response.text,'lxml').find_all('div',class_="article-list3-t") #爬取二级标题下的段落
    if os.path.exists('D:\\spy\\gld_url_all.html'):
        file = open('D:\\spy\\gld_url_all.html','a+',encoding='utf-8')
        con = str(con)
        file.write(con)
        file.close()
    else:
        file = open('D:\\spy\\gld_url_all.html','w+',encoding='utf-8')
        con = str(con)
        file.write(con)
        file.close()
    print(con)

#洗数据
if os.path.exists('d:\\spy\\gld_url_wash_1.txt'):
    os.remove('d:\\spy\\gld_url_wash_1.txt')
else:
    pass
file = open('d:\\spy\\gld_url_all.html','r+',encoding='utf-8')
for i in file.readlines():
    urls = re.findall(r'href="(.*?)"',i)
    if urls == []:
        continue
    else:
        pass
    url = str(urls)
    url = url.replace('[','')
    url = url.replace(']','')
    url = url.replace("'","")
    file = open('d:\\spy\\gld_url_wash_1.txt','a+',encoding='utf-8')    
    print(url)
    file.write(url+'\n')
    file.close()
file.close()




####pro5####
from bs4 import BeautifulSoup as soup
import requests
#print('默认编码格式为:',sys.getdefaultencoding())
#agent:Chrome
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'}
#while True:
    #url = input('请输入网址\n>>>')
url='http://url.club/'
try:
    response = requests.get(url,headers = header)
    #if response.status_code == 200:
    #    pass
    #else:
    #    print('输入网址不合法，请重新输入')
    response.encoding='utf-8' #强行转码
    con = soup(response.text,'lxml').find_all('h2') #爬取二级标题下的段落
    file = open('D:\\python\\contenct.html','a+',encoding='utf-8')
    con = str(con)
    file.write(con)
    file.close()
    print(con)
except Exception as e:
    print('输入错误，错误原因为:',e)
    
####pro4####
import re
import requests
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'}
url = 'http://image.so.com/index.html'
response = requests.get(url,headers = header)
src = re.findall(r'src="(.*?)"',response.text,re.I|re.S|re.M) #r代表原生字符串
print(src,'\n',name)

####pro3####
from bs4 import BeautifulSoup as soup
import requests
#print('默认编码格式为:',sys.getdefaultencoding())
#agent:Chrome
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'}
#while True:
    #url = input('请输入网址\n>>>')
url='http://url.club/'
try:
    response = requests.get(url,headers = header)
    if response.status_code == 200:
        pass
    else:
        print('输入网址不合法，请重新输入')
    response.encoding='utf-8' #强行转码
    con = soup(response.text,'lxml').find_all('h2') #爬取二级标题下的段落
    file = open('D:\\python\\contenct.html','a+',encoding='utf-8')
    con = str(con)
    file.write(con)
    file.close()
    print(con)
except Exception as e:
    print('输入错误，错误原因为:',e)


####pro2####
import time
import re
from bs4 import BeautifulSoup as soup
import requests
#print('默认编码格式为:',sys.getdefaultencoding())
#agent:Chrome
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'}
#while True:
    #url = input('请输入网址\n>>>')
url='http://url.club'
try:
    response = requests.get(url,headers = header)
    if response.status_code == 200:
        pass
    else:
        print('地址错误，请重新输入')
    response.encoding='utf-8' #强行转码
    #抓取title标签间的内容
    #contenct = re.findall(r'<title>(.*?)</title>',response.text)
    #print(contenct)
    #抓取超链接标签间的内容
    contenct = re.findall(r'<a.*?title=.*?href=.*?rel="bookmark">.*?</a>',response.text)
    file = open('D:\\python\\contenct.txt','w+',encoding='utf-8')
    contenct=str(contenct)
    file.writelines(contenct)
    file.close()
except Exception as e:
    print('输入错误，错误原因为:',e)

####pro1####
from bs4 import BeautifulSoup as soup
import requests
#print('默认编码格式为:',sys.getdefaultencoding())
#agent:Chrome
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'}
#while True:
    #url = input('请输入网址\n>>>')
url='http://url.club/'
try:
    response = requests.get(url,headers = header)
    if response.status_code == 200:
        pass
    else:
        print('输入网址不合法，请重新输入')
    response.encoding='utf-8' #强行转码
    con = soup(response.text,'lxml').find_all(h2) #爬取关键字的撮箕代码name
    file = open('D:\\python\\contenct.txt','a+',encoding='utf-8')
    con = str(con)
    file.write(con)
    file.close()
    print(con)
except Exception as e:
    print('输入错误，错误原因为:',e)
'''



'''
from bs4 import BeautifulSoup as soup
#import re
import requests
#print('默认编码格式为:',sys.getdefaultencoding())
#agent:Chrome
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'}
#while True:
    #url = input('请输入网址\n>>>')
url='http://vip.1905.com/?fr=homepc_menu_vip'
try:
    response = requests.get(url,headers = header)
    if response.status_code == 200:
        pass
    else:
        print('输入网址不合法，请重新输入')
    response.encoding='utf-8' #强行转码
    con = soup(response.text,'lxml').find_all('h3',class_="txt") #爬取关键字撮箕代码name
    file = open('D:\\Original\\contenct.txt','w+',encoding='utf-8')
    con = str(con)
    file.write(con)
    file.close()
    print(con)
except Exception as e:
    print('输入错误，错误原因为：\n',e)
'''
