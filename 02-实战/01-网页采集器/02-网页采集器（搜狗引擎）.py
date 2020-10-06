

# 爬取搜索引擎指定词条对应的搜索结果页面
# （简易网页采集器）


# UA伪装
# UA：User-Agent（请求载体的身份标识）
import requests

def getBaiduPage(queryParam):
    url = 'https://www.sogou.com/sogou'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0',
    }
    param = {
        'query': queryParam
    }
    response = requests.get(url=url, params=param, headers=headers)
    pageText = response.text
    filePathToSave = queryParam+'.html'
    with open(filePathToSave, 'w', encoding='utf-8') as f:
        f.write(pageText)
    print(filePathToSave, "保存成功！")
    return

if __name__ =='__main__':
    key = input("enter a key word:")
    getBaiduPage(key)
