# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import Rule, CrawlSpider
from scrapy.contrib.linkextractors import LinkExtractor


class CrawlSpiderdemo(CrawlSpider):
    name = "example"
    allowed_domains = ["example.com"]
    start_urls = [
        'http://www.example.com/1.html',
        'http://www.example.com/2.html',
        'http://www.example.com/3.html',
        ]

    rules = (
        # 提取匹配 'category.php' (但不匹配 'subsection.php') 的链接并跟进链接(没有callback意味着follow默认为True)
        Rule(LinkExtractor(allow=('category\.php'),deny=('subsection\.php'))),

        # 提取匹配 'item.php' 的链接并使用spider的parse_item方法进行分析
        Rule(LinkExtractor(allow=('item\.php')),callback='parse_item'),
    )


    def parse_item(self, response):
        self.log("this is an item page! %s" % response.url)

        item = scrapy.Item()
        item['id'] = response.xpath('//td[@id="item_id"]/text()').re(r'ID:(\d+)')
        item['name'] = response.xpath('//td[@id="item_name"]/text()').extract()
        item['description'] = response.xpath('//td[@id="item_description"]/text()').extract()
        return item

# CrawlSpider

# 爬取一般网站常用的spider，其定义了一些规则（rule）来提供跟进link的方便的机制。也许该spider并不是完全适合您的特定网站
# 或项目 因此您可以以其为起点  根据需求修改部分方法  当然您也可以实现自己的spider
#
# 除了从spider继承过来的属性之外 还有一个新的属性
# rules
#     一个包含一个或多个rule对象的集合(list) 每个rule对爬取网站的动作定义了特定表现
#
# parse_start_url(response)
#     当start_url的请求返回时 该方法被调用  该方法分析最初的返回值 并必须返回一个item对象或者一个request对象或者一个可迭代的包含二者的对象

# 爬取规则(Crawling rules)
# link_extractor 是一个Link Extractor 对象  其定义了如何爬取到页面提取链接

# callback 是一个或string 从link_extractor中每获取到链接时将会调用该函数 该回调函数接受一个Response作为其第一个参数，并返回一个
# 包含item以及request对象的列表（list）


# 当编写爬虫规则时，请避免使用 parse 作为回调函数。 由于 CrawlSpider 使用 parse 方法来实现其逻辑，
# 如果 您覆盖了 parse 方法，crawl spider 将会运行失败。

# cb_kwargs 包含传递给回调函数的参数(keyword argument)的字典。
#
# follow 是一个布尔(boolean)值，指定了根据该规则从response提取的链接是否需要跟进。 如果 callback 为None， follow 默认设置为 True ，否则默认为 False 。
#
# process_links 是一个callable或string(该spider中同名的函数将会被调用)。 从link_extractor中获取到链接列表时将会调用该函数。该方法主要用来过滤。
#
# process_request 是一个callable或string(该spider中同名的函数将会被调用)。 该规则提取到每个request时都会调用该函数。该函数必须返回一个request或者None。 (用来过滤request)














