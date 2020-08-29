# -*- coding:utf-8 -*-
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


if os.path.exists('biquge'):
    psaa
else:
    os.mkdir('biquge')


for i in range(1, len(webcontenct)):
    print(url+webcontenct[i][0],'\n')
    #请求太频繁会被拦截，设置间隔1S最佳
    time.sleep(1)
    response2 = requests.get(url+webcontenct[i][0])
    response2.encoding = 'utf-8'
    #<div id="content"><!--go--></div>
    contenct = soup(response2.text,'lxml').find_all('div', id="content")
    #replace处理内容转换成str类型
    contenct = str(contenct)
    if contenct == '[]':
        print(webcontenct[i], 'error!')
        #py_logger.error(str(url+webcontenct[i][0]))
    #处理数据
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
