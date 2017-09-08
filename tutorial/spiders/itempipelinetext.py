# -*- coding: utf-8 -*-

# Item Pipeline
#
# 当item在spider中被收集之后  他将会被传递到item pipeline，一些组件会按照一定的顺序执行对item的处理
#
# 每个item pipeline组件 是实现了简单方法的python类 他们接受到item并通过它执行一些行为，同时也决定此item是否继续通过pipeline
# 或者被丢弃而不再进行处理
#
# item pipeline一些典型的应用
# 1，清理html数据
# 2，验证爬取的数据（检查item包含哪些字段）
# 3，查重（并丢弃）
# 4，将爬取的结果保存到数据库中
#
# 每个item pipeline组件都是一个独立的python类 同时必须实现以下方法
# process_item(item, spider)
# 每个item pipeline组件都需要调用该方法，这个方法必须返回一个 Item (或任何继承类)对象， 或是抛出 DropItem 异常，被丢弃的item将不会被之后的pipeline组件所处理。
#
# 参数:
# item (Item 对象) – 被爬取的item
# spider (Spider 对象) – 爬取该item的spider
# 此外,他们也可以实现以下方法:
#
# open_spider(spider)
# 当spider被开启时，这个方法被调用。
#
# 参数:	spider (Spider 对象) – 被开启的spider
# close_spider(spider)
# 当spider被关闭时，这个方法被调用
#
# 参数:	spider (Spider 对象) – 被关闭的spider
import json
from scrapy.exceptions import DropItem


class pricepipeline(object):
    cat_factor = 1.15

    def process_item(self,item,spider):
        if item['price']:
            if  item['price_excludes_vat']:
                item['price'] = item['price']
            return item
        else:
            raise DropItem('missing price in %s' % item)

# 将item写入json文件

class JsonWriterPipeline(object):
    def __init__(self):
        self.file = open('items.jl','wb')

    def process_item(self,item,spider):
        line = json.dump(dict(item))+"\n"
        self.file.write(line)
        return item

#去重

# 一个用于去重的过滤器，丢弃那些已经被处理过的item。让我们假设我们的item有一个唯一的id，
# 但是我们spider返回的多个item中包含有相同的id:

class DuplicatesPipeline(object):

    def __init__(self):
        self.ids_seen = set()

    def process_item(self,item,spider):
        if item['id'] in self.ids_seen:
            raise DropItem("Duplicate item found: %s " % item)
        else:
            self.ids_seen.add(item['id'])
            return item

# 启用一个Item Pipeline组件
# 为了启用一个Item Pipeline组件，你必须将它的类添加到 ITEM_PIPELINES 配置
# ITEM_PIPELINES = {
#     'myproject.pipelines.PricePipeline': 300,
#     'myproject.pipelines.JsonWriterPipeline': 800,
# }


# 数据收集
#
# scrapy提供了方便手机数据的机制 数据已key/value方式存储  值大多是计数值 该机制叫做数据收集器













