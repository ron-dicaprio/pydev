# -*- coding:utf-8 -*-
import urllib.request
import urllib.parse
import json
def youdao_translate(content):
    youdao_url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    data = {}
    # 调接口时所需参数
    data['i'] = content
    data['from'] = 'AUTO'
    data['to'] = 'AUTO'
    data['smartresult'] = 'dict'
    data['client'] = 'fanyideskweb'
    data['salt'] = ''
    data['sign'] = ''
    data['doctype'] = 'json'
    data['version'] = '2.1'
    data['keyfrom'] = 'fanyi.web'
    data['action'] = 'FY_BY_CLICKBUTTION'
    data['typoResult'] = 'false'
    data = urllib.parse.urlencode(data).encode('utf-8')
    # 发送翻译请求
    try:
        youdao_response = urllib.request.urlopen(youdao_url, data)
    # 获得响应
        youdao_html = youdao_response.read().decode('utf-8')
    except Exception as e:
        print(e)
    target = json.loads(youdao_html)
	# 取出需要的数据
    trans = target['translateResult'][0][0]['tgt']
    return trans
