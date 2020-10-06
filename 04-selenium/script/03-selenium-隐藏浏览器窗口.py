

from selenium import webdriver
from selenium.webdriver.chrome.options import Options   #导入这个类
import time

# 实例化Options对象
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

driver_path = '../chromeDriver/chromedriver.exe'
# 设置无头浏览器Options
browser  = webdriver.Chrome(driver_path, chrome_options=chrome_options)
# webdriver.phantomjs：已经封装好了的无头浏览器，但已经停止更新和维护了

url = 'https://www.baidu.com'
browser.get(url)

page_text = browser.page_source
print(page_text)


time.sleep(5)
browser.quit()

