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
