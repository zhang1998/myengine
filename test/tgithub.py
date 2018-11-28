
from selenium import webdriver

import time

from selenium.webdriver.common.keys import Keys

'''
访问淘宝
'''
browser = webdriver.Firefox()
browser.get("https://github.com/search?json")
input_str = browser.find_element_by_class_name('q')
input_str.send_keys("time") #原来是通过按键实现了功能
input_str.send_keys(Keys.ENTER)   #通过回车键来代替鼠标的左键
button = browser.find_element_by_class_name('btn-search')
button.click()


