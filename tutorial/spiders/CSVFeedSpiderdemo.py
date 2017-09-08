# -*- coding: utf-8 -*-
import scrapy
from scrapy import log
from scrapy.spiders import CSVFeedSpider
from tutorial.items import TutorialItem


class CSVFeedSpiderdemo(CSVFeedSpider):
    name = "exampledemos"
    allowed_domains = ["CSVFeedSpider"]
    start_urls = ['http://www.example.com/feed.csv']
    delimiter = ';'
    headers = ['id','name','description']

    def parse_row(self, response,row):
        log.msg('this is a row!: %r' % row)

        item = TutorialItem()
        item['id'] = row['id']
        item['name'] = row['name']
        item['description'] = row['description']
        return item


# CSVFeedSpider
# 该spider除了按行遍历而不是节点之外其他和XMLFeedSpider十分类似 而其在每次迭代是调用的是parse_row()
#
# delimiter
# 在CSV文件中用于区分字段的分隔符。类型为string。 默认为 ',' (逗号)。
#
# headers
# 在CSV文件中包含的用来提取字段的行的列表。参考下边的例子。
#
# parse_row(response, row)
# 该方法接收一个response对象及一个以提供或检测出来的header为键的字典(代表每行)。 该spider中，您也可以覆盖 adapt_response 及 process_results 方法来进行预处理(pre-processing)及后(post-processing)处理。