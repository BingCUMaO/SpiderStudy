
#导入requests包
import requests
if __name__ == '__main__':
    # 1、指定url
    url = 'https://www.baidu.com'
    #2、发起请求
    response = requests.get(url)
    #3、获取响应对象
    page = response.text
    print(page)
    #4、持久化存储
    with open('spiderPage.html', 'w', encoding='utf-8') as sf:
        sf.write(page)

    print("爬取结束")

