
### 创建Scrapy工程：
- scrapy startproject projectName

### 工程创建完成后，在spiders子目录中创建一个爬虫文件

- cd projectName
- scrapy genspider spiderFileName www.xx.com


### 当爬虫写完之后，执行工程

 - scrapy crawl spiderFileName



### 创建以CrawlSpider为父类的爬虫文件

- scrapy genspider -t crawl spiderFileName www.xx.com


 # 持久化储存

 1、 基于终端指令：这种基于终端指令的方式，只能将parse方法的返回值存储到本地的文本文件中（其中所存储的文本格式有限制要求）
 - scrapy crawl spiderFileName -o ./saveFilePath


 2、 基于管道：

 - 编码流程
    - 数据解析
    - 在item类中定义相关的属性
    - 将解析的数据封装存储到item类型的对象中
    - 将item类型的对象提交给管道进行持久化存储的操作
    - 在管道类的process_item中要将其接受到的item对象中存储的数据进行持久化存储操作
    - 在配置文件中开启管道功能
    
    
    
