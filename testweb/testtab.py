#通过执行js打开新的标签页
import time

from selenium import webdriver

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()
#通过执行js打开新的标签页
js='window.open("https://www.sogou.com");'

driver.get("https://www.sogou.com")
driver.execute_script(js)


#覆盖之前的标签页

driver.find_element_by_class_name('btn').send_keys(Keys.CONTROL,'t')      #Ctrl+t在Chrome下新建标签页，这里只能覆盖

driver.get("https://www.sogou.com")


