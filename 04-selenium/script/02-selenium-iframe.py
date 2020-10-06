
# 模拟iframe标签下的鼠标拖动

from selenium import webdriver
from selenium.webdriver import ActionChains     #导入动作链类
import time

driver_path = '../chromeDriver/chromedriver.exe'
browser = webdriver.Chrome(driver_path)

url = 'https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)

# 如果定位的标签是存在于iframe标签之内的，则必须通过如下操作进行标签定位
browser.switch_to.frame('iframeResult')         # 切换浏览器标签定位的作用域
div = browser.find_element_by_id('draggable')


# 动作链
action = ActionChains(browser)
action.click_and_hold(div)          #点击长按指定的标签

for i in range(5):
    print(i)
    # perform() 表示立即执行动作链的操作
    action.move_by_offset(17, 0).perform()

#释放动作链对象
action.release()

time.sleep(5)
browser.quit()