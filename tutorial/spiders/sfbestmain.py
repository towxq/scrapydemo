# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import sfitem
from scrapy.selector import Selector


class SfbestmainSpider(scrapy.Spider):
    name = "sfbestmain"
    allowed_domains = ["m.sfbest.com"]
    start_urls = ['https://m.sfbest.com/category/categoryDetail?isOversea=2&categoryId=1&searchValue=7421,7423&pageNo=1']

    def parse(self, response):
        # items = response.xpath('//html/body/div[@class="content"]/div[@class="list-pannel jscroll"]/div[@class="jscroll-inner clearfix"]/div[@class="p-list clearfix"]')
        try:
            items = response.xpath('//div[@class="fl p-info"]')
            print type(items)
        except Exception,e:
            print str(e.args)

        for item in items:
            sitem = sfitem()
            sitem['url'] = item.xpath('//a/@href').extract()
            # sitem['id'] = item.xpath('//*[@id="add_cart"]/@productid')
            sitem['productname'] = item.xpath('//div[1]/div/a[1]/div[1]/text()').extract()
            sitem['price'] = item.xpath('//div[1]/div/a[1]/div[3]/div[1]/div/span/text()').extract()+item.xpath('//div[1]/div/a[1]/div[3]/div[1]/div/text()[2]').extract()
            yield sitem

        # sfitems = sfitem()
        # sfitems['url'] = response.url
        # sfitems['id'] = response.xpath('//*[@id="productid"]/@value').extract()[0]
        # sfitems['productname'] = response.xpath('//*[@id="product-info"]/section[1]/h1/text()').extract()
        # sfitems['price'] = response.xpath('//*[@id="product-info"]/section[1]/div/span[1]/em/text()').extract()[0]+response.xpath('//*[@id="product-info"]/section[1]/div/span[1]/text()[2]').extract()[0]
        # yield sfitems