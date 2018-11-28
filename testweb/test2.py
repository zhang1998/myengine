#-*-coding:utf-8-*-

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

test=["http://www.github.com","https://www.jb51.net/","https://www.iplaysoft.com/","https://www.cnblogs.com/","https://www.baidu.com/","https://github.com/issues",
      "http://www.soyunpan.com/","http://www.pansou.com/","http://www.iwapan.com/","http://www.verypan.com/","https://www.panc.cc/","http://www.xilinjie.com/"]
for element in test:
    browser = webdriver.Firefox()
    browser.get(element)
    source = browser.find_element_by_name('q')
    source.send_keys("all")
    source.send_keys(Keys.ENTER)