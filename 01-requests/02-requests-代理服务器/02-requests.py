import requests

url = 'https://www.baidu.com/s?wd=ip'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
}
proxies={
    "https": '222.110.147.50:3128'
}
# 在requests的请求参数中添加代理服务器的协议和ip
requests.get(url=url, headers=headers, proxies=proxies)