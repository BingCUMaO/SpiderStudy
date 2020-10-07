import scrapy

# 导入item.py文件中的DataparseItem类
from dataparse.item import DataparseItem


class BingcuSpider(scrapy.Spider):
    name = 'bingcu'
    allowed_domains = ['www.qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/']

    # 基于终端指令
    # def parse(self, response):
    #     # 解析：作者的名称+段子
    #     div_list = response.xpath('//div[@id="content-left"]/div')
    #     print(div_list)
    #     for div in div_list:
    #         # xpath返回的是列表，但是列表元素一定是Selector类型的对象
    #         # extract()方法可以将Selector对象中data参数储存的字符串提取出来
    #         # autor = div.xpath('./div[1]/a[2]/h2/text()')[0]extract()
    #         author = div.xpath('./div[1]/a[2]/h2/text()').extract_first()
    #         # 列表调用了extract之后，则表示将列表中的每一个Selector对象中data对应的字符串提取出来
    #         content = div.xpath('./a[1]/div/span//text()').extract()
    #         content = ''.join(content)
    #
    #         print(author, content)

    # 基于管道
    def parse(self, response):
        # 解析：作者的名称+段子
        div_list = response.xpath('//div[@id="content-left"]/div')
        print(div_list)
        for div in div_list:
            # xpath返回的是列表，但是列表元素一定是Selector类型的对象
            # extract()方法可以将Selector对象中data参数储存的字符串提取出来
            # autor = div.xpath('./div[1]/a[2]/h2/text()')[0]extract()
            author = div.xpath('./div[1]/a[2]/h2/text()').extract_first()
            # 列表调用了extract之后，则表示将列表中的每一个Selector对象中data对应的字符串提取出来
            content = div.xpath('./a[1]/div/span//text()').extract()
            content = ''.join(content)

            print(author, content)


            #实例化item对象
            item = DataparseItem()
            item['author'] = author
            item['content'] = content

            #将item提交给了管道
            yield item