# -*- encoding:utf-8 -*-
import os
import datetime
if os.path.exists('logs'):
    pass
else:
    os.mkdir('logs')
'''
#another kind of time format 
datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
'''
def info(self):
    file = open('logs/%s.wrapper' % (datetime.datetime.now().date()),'a+',encoding='utf-8')
    file.writelines('###  %s |info| %s\n' % (datetime.datetime.now(),str(self)))
    file.close()
    
def warnnig(self):
    file = open('logs/%s.wrapper' % (datetime.datetime.now().date()),'a+',encoding='utf-8')
    file.writelines('###  %s |warn| %s\n' % (datetime.datetime.now(),str(self)))
    file.close()
    
def error(self):
    file = open('logs/%s.wrapper' % (datetime.datetime.now().date()),'a+',encoding='utf-8')
    file.writelines('###  %s |erro| %s\n' % (datetime.datetime.now(),str(self)))
    file.close()
'''
#i do not like this kind of expression
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
'''
