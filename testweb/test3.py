#-*-coding:utf-8-*-
from selenium import webdriver


from selenium.webdriver.common.keys import Keys

test=["https://www.jb51.net","https://www.iplaysoft.com/","https://www.cnblogs.com/","http://www.github.com","https://www.baidu.com/","https://github.com/issues",
      "http://www.soyunpan.com/","http://www.pansou.com/","http://www.iwapan.com/","http://www.verypan.com/","https://www.panc.cc/","http://www.xilinjie.com/"]
'''
driver = webdriver.Firefox()
#通过执行js打开新的标签页
for element in test:
    #js='window.open("https://www.sogou.com");'
    js='window.open('+"https://www.jb51.net"+');'
    driver.get(element)
    driver.execute_script(js)
    #覆盖之前的标签页
    driver.find_element_by_class_name('btn').send_keys(Keys.CONTROL,'t')      #Ctrl+t在Chrome下新建标签页，这里只能覆盖
    #driver.get("https://www.sogou.com")
    driver.get(element)


'''
driver = webdriver.Firefox()
#通过执行js打开新的标签页
js='window.open("https://www.jb51.net");'

driver.get("https://www.jb51.net")
driver.execute_script(js)


#覆盖之前的标签页

driver.find_element_by_class_name('btn').send_keys(Keys.CONTROL,'t')      #Ctrl+t在Chrome下新建标签页，这里只能覆盖



driver.find_element_by_class_name('btn').send_keys(Keys.CONTROL,'l')


