

# 直接拿来用
import time

from selenium.webdriver.chrome.options import Options   #无头浏览器的Options类
from selenium import webdriver
from selenium.webdriver import ChromeOptions    # 规避检测用的类

# 规避配置
option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])

# 实例化Options对象
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')



# 驱动路径
driver_path = '../chromeDriver/chromedriver.exe'
# 设置无头浏览器Options和规避反爬配置参数
browser  = webdriver.Chrome(driver_path, chrome_options=chrome_options, options=option)




url = 'https://www.baidu.com'
browser.get(url)
print(browser.page_source)

time.sleep(5)
browser.quit()
