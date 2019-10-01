# -*-coding:utf-8 -*-
#!/usr/bin/env python
#普通二维码生成器
import qrcode
import datetime
import os
import pylog
while 1:
    contenct = input('请输入二维码内容\n>>>')
    if len(contenct) >50:
        print('输入字符过长！请输入小于50字符')
        continue
    else:
        break
current_time=datetime.datetime.now().strftime("%Y%m%d%H%M%S")
pylog.logger.info(current_time)
print(current_time)
if os.path.exists('images'):
    pass
else:
    os.mkdir('images')
qr_img= qrcode.make('%s' % (contenct))
qr_img.save('images/%s.png' % (current_time))
print('file saved！',os.getcwd()+'\\images\\'+current_time+'.png')
#打开二维码
qr_img.show()
print('programm exit')
exit()
