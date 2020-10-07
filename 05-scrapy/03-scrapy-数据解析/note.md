### 基于Spider 的全站数据解析

- 就是将文章中某板块下的全部页码对应的页面数据进行爬取
- 需求：爬取文章中的照片的名称
- 实现方式：
    - 第一种方式：将所有页面的url添加到start_urls列表中（不推荐）
    - 第二种方式：手动进行网络请求发送（推荐）
        - 在parse(self, response)方法中，添加如下格式的代码：yield scrapy.Request(url=url, callback=callback_func)
        - 其中callback专门用作于数据解析（可以是递归回调，只要加个递归基就行了）
        
        
        
        
### 请求传参
- 其实就是将item对象传到yield scrapy.Request(url=url, callback=callback_func)中的callback_func方法里，使得callback_func方法内部能读取到原来的parse()方法中的item对象的其他属性值
- yield scrapy.Request(url=url, callback=callback_func, meta={'item': item})
- callback_func方法里面，可以通过item = response.meta\['item']来接收meta





### ImagesPipeline

- 使用：只需要将img的src的属性值进行解析，提交到管道，管道就会对图片的src进行请求发送获取图片的二进制数据，并进行持久化操作
- 需求：爬取站长素材中的高清图片
- 使用流程
  - 数据解析（解析出图片的url）
  - 将储存图片地址的item提交到指定的管道类
  - 在管道文件中自定义一个基于ImagesPipeLine父类的管道类（重写ImagesPipeline类的3个方法）
    - getmedia_request
    - file_path
    - item_completed
  - 在配置文件中：
    - 指定图片存储的目录：IMAGES_STORE = './imgs/'
    - 指定所要开启的管道：自定义的管道类

