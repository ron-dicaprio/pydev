import requests
import json
def dingtalk(contenct,keyword):
    token='token'
    webhook = 'https://oapi.dingtalk.com/robot/send?access_token=%s' % (token)
    chorme_header  = {"Content-Type": "application/json","Charset": "UTF-8"}
    contenct = keyword + ':' + contenct
    message = {
        "msgtype": "text",
        "text": {
            "content": contenct
        },
        "at": {
            #是否@所有人，Ture or False
            "isAtAll": False
        }

    }
    # 对请求的数据进行json封装
    message_json = json.dumps(message)
    print('json格式为：',message_json)
    # 发送请求
    try:
        info = requests.post(url=webhook, data=message_json, headers=chorme_header)
        # 打印返回的结果
        print('消息发送成功!返回信息为：', info.text)
    except Exception as e:
        print(e)

        
'''
import requests,json,sys

def dingtalk(contenct,is_atall=False):
    webhook = 'https://oapi.dingtalk.com/robot/send?access_token=364e8a54b3a0f8f65cb44daa0af76e3b57cc0687e1d1a67497da6f8d5f36660a'
    chorme_header  = {"Content-Type": "application/json","Charset": "UTF-8"}
    contenct = '智能小助手' + ':' + contenct
    # contenct = '智能小助手' + ':' + sys.argv[1]  # 传参
    message = {
        "msgtype": "text",
        "text": {
            "content": contenct
        },
        "at": {
            #是否@所有人，Ture or False
            "isAtAll": is_atall
        }
    }
    # 对请求的数据进行json封装
    message_json = json.dumps(message)
    print('json格式为：',message_json)
    # 发送请求
    try:
        info = requests.post(url=webhook, data=message_json, headers=chorme_header)
        # 打印返回的结果
        print('消息发送成功!返回信息为：', info.text)
    except Exception as E:
        print('消息发送失败!返回信息为：', E)


dingtalk('check interface',False)
'''
