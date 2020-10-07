# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class DataparsePipeline:
    fp = None

    # 重写父类的一个方法：该方法只会在开始爬虫的时候被调用一次
    def open_spider(self, spider):
        print('爬虫开始......')
        filePath = './save.txt'
        self.fp = open(filePath, 'w', encoding='utf-8')

    # 重写父类的一个方法：该方法只会在结束爬虫的时候被调用一次
    def close_spider(self, spider):
        self.fp.close()
        print('爬虫结束！')


    # 专门用来处理item类型对象
    # 该方法可以接受爬虫文件提交过来的item对象
    # 该方法每接收到一个item就会被调用一次
    def process_item(self, item, spider):
        author = item['author']
        content = item['content']

        # 持久化存储操作
        self.fp.write(author+':'+content+'\n')

        # 如果需要两个管道类，一个存储到本地，一个存储到数据库
        # return操作会把item传递给下一个管道类进行存储操作
        # 因此每次操作完管道类之后的好习惯是return传入的item对象
        return item

