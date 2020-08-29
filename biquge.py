# -*- coding:utf-8 -*-
#re和bs4同时间使用效果还不错
import lxml
import re
import os
import py_logger
import time
from bs4 import BeautifulSoup as soup
import requests
chorme_header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2652.2 Safari/537.36'}
url = input('请输入笔趣阁小说下载地址:\n')
response1 = requests.get(url, headers = chorme_header)
response1.encoding = 'utf-8'

title = re.findall(r'<h1>(.*?)</h1>', response1.text)[0]
webcontenct = re.findall(r'a href="(.*?)" title="(.*?)"', response1.text)

#创建文件夹
if os.path.exists(r'biquge'):
    pass
else:
    os.mkdir(r'biquge')

for i in range(0, len(webcontenct)):
    print(url+webcontenct[i][0],'\n')
    #请求太频繁会被拦截，设置间隔1S以上最佳
    time.sleep(1.2)
    response2 = requests.get(url+webcontenct[i][0], headers = chorme_header)
    response2.encoding = 'utf-8'
    #<div id="content"><!--go--></div>
    contenct = soup(response2.text,'lxml').find_all('div', id="content")
    #replace处理内容转换成str类型
    contenct = str(contenct)
    #判断获取内容状态，如果是空，再次发起请求
    if contenct == '[]':
        time.sleep(2)
        response3 = requests.get(url+webcontenct[i][0], headers = chorme_header)
        response3.encoding = 'utf-8'
        contenct = soup(response3.text, 'lxml').find_all('div', id="content")
        #如果仍然是空，打印提示
        if contenct == '[]':
            py_logger.error(str(url+webcontenct[i][0]))
            print('error!', url + webcontenct[i][0])
        else:
            pass

    #replace处理数据
    else:
        contenct = contenct.replace('<br/>', '')
        contenct = contenct.replace('[<div id="content"><!--go-->', '')
        contenct = contenct.replace('<!--over-->', '')
        contenct = contenct.replace('</div>]', '')

    print(contenct)

    with open(r'biquge\\%s.txt'% (title), 'a+', encoding='utf-8' ) as file:
        #写入标题和内容
        file.write('%s\n%s' % (webcontenct[i][1], contenct))
        file.close()
