# demo.py

'''

#-*- coding:utf-8 -*-
#!/usr/bin/env python
import requests,json
appID='wx44bbfdcb7e7678a2'
appsecret='e94dd044a15a53d57bfdd5882ddf4ca7'

# 获取微信的access_token
def getapptoken():
    weburl='https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s' % (appID,appsecret)
    try:
        getapptoken_res=json.loads(requests.get(weburl).content)
        return getapptoken_res["access_token"]
    except Exception as e:
        print(e)
        return None

temp_token=getapptoken()
errortime='7200'

# 获取微信服务器的IP地址
def getwxhostip():  
    weburl='https://api.weixin.qq.com/cgi-bin/get_api_domain_ip?access_token=%s' % (temp_token)
    try:
        getwxhostip_res=json.loads(requests.get(weburl).content)
        return getwxhostip_res["ip_list"]
    except Exception as e:
        print(e)
        return None




print(getwxhostip())

#-*- coding:utf-8 -*-
#!/usr/bin/env python
from pywebio import output,start_server,input
import pandas

def main():
    height = input.input("请输入你的身高(cm)：", type=input.FLOAT)    
    output.put_text(height)

    output.put_text('这是一个表格')
    # 插入一个表格
    output.put_table(
        tdata=[
            ['序号', '姓名', '年龄', '性别', '备注'],
            ['1', 'name', 'age', 'sex', 'rsrv']
        ]
    )
      
    output.put_markdown('# 文件识别程序')
    output.put_markdown('## 功能描述：')
    output.put_markdown(

    - 点击上传文件
    - 加载并输出表格内容

    )
    
    file = input.file_upload('请选择文件', '.xlsx',placeholder='点击此处上传xlsx文件')
    output.toast('文件上传成功!')
    df = pandas.read_excel(file['content'])
    output.put_html(df.head(10).to_html())
    
    
if __name__=='__main__':
    start_server(main, port=8080, debug=True, cdn=False,auto_open_webbrowser=True,reconnect_timeout=3000)
    #start_server(main, port=8080, debug=True, cdn=False,auto_open_webbrowser=True,reconnect_timeout=3000,remote_access=True)

        

from pywebio.input import input, FLOAT
from pywebio.output import put_text
def bmi():    
    height = input("请输入你的身高(cm)：", type=FLOAT)    
    weight = input("请输入你的体重(kg)：", type=FLOAT)    
    BMI = weight / (height / 100) ** 2    
    top_status = [(14.9, '极瘦'), (18.4, '偏瘦'), (22.9, '正常'), (27.5, '过重'),(40.0, '肥胖'), (float('inf'), '非常肥胖')]    
    for top, status in top_status:        
        if BMI <= top:            
            put_text('你的 BMI 值: %.1f，身体状态：%s' % (BMI, status))            
            break
if __name__ == '__main__':    
    bmi()



from pywebio.input import PASSWORD, file_upload,input_group,select,checkbox,radio,textarea,TEXT,NUMBER,input
from pywebio.output import put_text,put_table

# Text Output
data = input_group("Basic info", [ # 1
        input("what's name", type=TEXT, placeholder='This is placeholder',
              help_text='This is help text', required=True, name="name"),
        input("How old are you?", type=NUMBER, name="age"), # 2
        # Password input
        input("Input password", type=PASSWORD, name="password"),

        # Drop-down selection
        select('Which gift you want?', ['keyboard', 'ipad'], name="gift"),

        # Checkbox
        checkbox("User Term", options=['I agree to terms and conditions'], name="term"),

        # Single choice
        radio("Choose one", options=['A', 'B', 'C', 'D'], name="choose"),

        # Multi-line text input
        textarea('Text Area', rows=3, placeholder='Some text', name="text"),

        textarea('Code Edit', code={
            'mode': "python",
            'theme': 'darcula',
        }, value='import something\n# Write your python code', name="code"),
        # File Upload
        file_upload("Select a image:", accept="image/*", name="file")
    ])

# Password input
password = input("Input password", type=PASSWORD)

# Drop-down selection
gift = select('Which gift you want?', ['keyboard', 'ipad'])

# Checkbox
agree = checkbox("User Term", options=['I agree to terms and conditions'])

# Single choice
answer = radio("Choose one", options=['A', 'B', 'C', 'D'])

# Multi-line text input
text = textarea('Text Area', rows=3, placeholder='Some text')

# File Upload
img = file_upload("Select a image:", accept="image/*") 
'''
