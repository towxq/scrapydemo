# -*- coding: utf-8 -*-
import scrapy


class JddomainSpider(scrapy.Spider):
    name = "jddomain"
    allowed_domains = ["jd.com"]
    start_urls = ['https://m.sfbest.com/product/info/268277']

    def parse(self, response):
        # url = response.url
        # name = response.xpath('/html/body/div[5]/div/div[2]/div[1]/text()').extract()
        # price = response.xpath('/html/body/div[5]/div/div[2]/div[4]/div/div[1]/div[2]/span/span[2]')
        # print "----------------",url,name
        pass