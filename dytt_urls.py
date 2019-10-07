# -*- coding:utf-8 -*-
#@authur caitao
#caitao:我就是不写注释
import requests
import re
import os
if os.path.exists('logs'):
    if os.path.exists('logs\\dytt_urls.txt'):
        os.remove('logs\\dytt_urls.txt')
else:
    os.mkdir('logs')
print('文件存储路径为：'+os.getcwd()+'\\logs')
chorme_header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2652.2 Safari/537.36'}
for h in range(1,100):
    if h== 1:
        url = 'https://www.dytt8.net/html/gndy/dyzz/index.html'
    else:
        url = 'https://www.dytt8.net/html/gndy/dyzz/list_23_%d.html' % (h)
    print(url)
    response_url = requests.get(url, headers=chorme_header)
    #习惯性的utf-8
    response_url.encoding = 'utf-8'
    target_url = re.findall(r'a href="(.*?)" class="ulink"', response_url.text)
    for n in range(0, len(target_url)):
        with open('logs/dytt_urls.txt', 'a+') as file:
            file.writelines('https://www.dytt8.net' + target_url[n] + '\n')
            file.close()
