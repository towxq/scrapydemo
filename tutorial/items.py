# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()、
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()
    pass

# 项目中的item文件
# item是保存爬取到的数据的容器  使用方法和python的字典类似