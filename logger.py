import time
import os
if os.path.exists('d:\\spy'):
    #print('file exists!')
    pass
else:
    os.mkdir('d:\\spy')
filenamedate = str(time.strftime('%Y-%m-%d',time.localtime(time.time())))
class pylog(object):
    def info(self):
        file = open('d:\\spy\\loginfo_%s.wrapper' % (filenamedate),'a+',encoding='utf-8')
        file.writelines(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) +'  '+ str(self) + '\n')
        file.close()
