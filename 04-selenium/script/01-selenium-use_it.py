

from selenium import webdriver
from lxml import etree
import time

kw = input("请输入搜索关键字：")
# 浏览器驱动
driver_path = '../chromeDriver/chromedriver.exe'

# 实例化了一个浏览器对象
browser = webdriver.Chrome(executable_path=driver_path)

browser.get('https://www.baidu.com')

search_kw = browser.find_element_by_id('kw')
search_go = browser.find_element_by_id('su')

search_kw.send_keys(kw)
search_go.click()

time.sleep(10)
browser.quit()