# -*- coding: utf-8 -*-
# !usr/bin/env python
from selenium import webdriver
import requests
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
chorme_header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2652.2 Safari/537.36'}

web_browser = webdriver.Chrome(executable_path=(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'))

weburl = 'https://www.asmrv.com/888.html'
#没必要去去httpstatu,浪费时间了
#httpcode = requests.get(weburl, headers = chorme_header).status_code
web_browser.maximize_window()
web_browser.get(weburl)
print('1')
try:
    #cont = web_browser.find_element_by_xpath('//*[@id="my-video"]')
    #cont = web_browser.find_elements_by_css_selector("#my-video_html5_api")
    print(web_browser.get(weburl).read())
    #cont = web_browser.find_elements_by_id("#my-video_html5_api")


    print(cont)

    #web_browser.find_element_by_id('fm-login-id').click()
    #web_browser.find_element_by_id('fm-login-id').send_keys('1102346940@qq.com')
    #web_browser.find_element_by_id('fm-login-password').send_keys('password')
    #先执行点击操作,
    #web_browser.find_element_by_xpath("//button[@tabindex='3']").click()
    #("//input[@type='submit' and @value='something']").click()
    #web_browser.find_element_by_xpath("//[@type='submit']").click()
    #nc_1__scale_text
    #web_browser.find_element_by_id('nc_1__scale_text')
    #WebDriverWait(web_browser, 5)
    #ActionChains(web_browser).drag_and_drop_by_offset(web_browser.find_element_by_xpath("//*[@id='nc_1_n1z']"), 280, 0).perform()
    #等待js加载
    WebDriverWait(web_browser, 5)
    #点击登陆按钮 其实也可以直接回车
    #web_browser.find_element_by_xpath("//button[@tabindex='3']").click()
    #time.sleep(5)
    #web_browser.get_screenshot_as_file('d:\\python_file\\%s.png' % (time.strftime('%Y-%m-%d-%H-%M-%S')))
    #print('截图成功！')
except Exception as E:
    print(E)
    web_browser.close()
