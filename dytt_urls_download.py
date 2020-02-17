# -*- coding:utf-8 -*-
#@authur caitao
#caitao:我就是不写注释
import requests
import re
import os
import sys
print('当前系统编码方式为:',sys.getfilesystemencoding())
chorme_header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2652.2 Safari/537.36'}
print(os.getcwd())
with open('logs/dytt_urls.txt','r+') as file:
    for url in file.readlines():
        url =url.replace('\n','')
        print(url)
        response_con = requests.get(url,headers = chorme_header)
        response_con.encoding = 'gbk'
        target_url = re.findall(r'"#fdfddf"><a href="(.*?)">ftp',response_con.text)
        print(target_url)
        if not os.path.exists('down_urls.txt'):
            with open('down_urls.txt','a+') as tmpfile:
                tmpfile.close()
        else:
            pass
        with open('down_urls.txt','a+') as downlink:
            downlink.writelines('%s\n' % (target_url))
            downlink.close()
    file.close()

