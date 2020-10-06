


import requests
import json

if __name__ == '__main__':
    postUrl = 'https://fanyi.baidu.com/sug'
    userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0"
    headers = {
        'User-Agent': userAgent
    }
    key = input("enter the key word:")
    param = {
        'kw': key
    }
    response = requests.post(url=postUrl, data=param, headers=headers)
    dictJson = response.json()
    print(dictJson)

    # 持久化存储
    fileName = key+'.json'
    fp = open(fileName, 'w', encoding='utf-8')
    json.dump(dictJson, fp = fp, ensure_ascii=False)   # 注意这里要将Ascii码关闭
    print(fileName,"保存成功！")
