

from selenium import webdriver
from lxml import etree
from selenium.webdriver import ActionChains
import time
import requests
import asyncio
import aiohttp
import uuid
import os
import io


def download_imgs(url_set, kw):
    headers = {
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
    }
    # 创建输入关键词的对应文件夹
    dir_path = "./"+kw+'/'
    os.makedirs(dir_path, exist_ok=True)

    # 定义单个图片抓取的协程方法
    async def crawl_img(url):
        # 设置图片名称和路径
        img_name = uuid.uuid4().__str__() + "." + url.split('.')[3]
        file_path = dir_path + img_name
        # 发送请求
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as response:
                # 读取二进制流并进行存储
                img_data =  await response.read()
                with open(file_path, 'wb') as fp:
                    fp.write(img_data)

    # 协程管理
    loop = asyncio.get_event_loop()
    tasks = []
    for url in  url_set:
        task = asyncio.ensure_future(crawl_img(url))
        tasks.append(task)

    # 执行协程列表
    loop.run_until_complete(asyncio.wait(tasks))

label = "=============================================================="
print(label)
kw = input("请输入搜索关键字：")
print(label)
print("推荐数值区间：[  1, 100  ]")
print("Tip:  装载因子越大下载的图片数越多，同时下载的时间越长")
factor = int( input("请输入装载因子："))
print(label)

# 开始时间记录
start_time = time.time()

# 浏览器驱动
driver_path = '../../chromeDriver/chromedriver.exe'

# 实例化了一个浏览器对象
browser = webdriver.Chrome(executable_path=driver_path)

# 跳转百度主页
browser.get('https://www.baidu.com')
search_kw = browser.find_element_by_id('kw')
search_go = browser.find_element_by_id('su')
search_kw.send_keys(kw)
search_go.click()

#跳转百度图片
img_page_url = 'http://image.baidu.com/i?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word='+kw
browser.get(img_page_url)

# 抓取图片的urls
img_urls_list = list()
print("抓取中，请耐心等待...")
for tick in range(factor):
    page_text = browser.page_source
    img_urls = etree.HTML(page_text).xpath('//*[@id="imgid"]/div/ul/li/div/a/img/@data-imgurl')
    img_urls_list.extend(img_urls)
    # 模拟鼠标滚轮事件，滚到当前页面的底部（未加载区域的顶部）
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

# 对urls进行去重
img_urls_set = set(img_urls_list)

# 根据图片的url列表，开始图片的下载动作
download_imgs(img_urls_set, kw)
print(label)
print("抓取结束！共抓取了%s张图片~"%len(img_urls_set))


browser.quit()
# 结束时间记录
end_time = time.time()
print("运行时间共花费：%.2f s"%round(end_time-start_time, 2))








