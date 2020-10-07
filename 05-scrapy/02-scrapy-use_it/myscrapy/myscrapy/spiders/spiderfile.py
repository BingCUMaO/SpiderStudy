import scrapy


class SpiderfileSpider(scrapy.Spider):
    name = 'spiderfile'
    # 允许的域名：用来限定start_url哪些url可以进行请求的发送
    # 一般不使用allowed_domains
    allowed_domains = ['www.baidu.com']
    # 起始的url列表：该列表中存放的url会被scrapy自动进行请求的发送
    start_urls = ['https://www.baidu.com/', 'https://www.sougou.com/']

    # 数据解析
    def parse(self, response):
        print(response)
