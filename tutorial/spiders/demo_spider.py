# -*- coding: utf-8 -*-
import scrapy

__author__ = '01210367'

# spider是用户编写的用于从单个网站(或者一些网站)爬取数据的类
#
# 包含一个用于下载的URL，如何跟进网页中的链接以及如何分析页面中的内容  提取生成的item的方法


class DemoSpider(scrapy.Spider):
    # name用于区别spider 唯一
    name = "demospider"
    # 包含了spider允许爬取的域名列表 当offsiteMiddleware启用时 域名不存在列表中的URL不会被跟进
    allowed_domains = ["demo.org"]
    # start_urls包含了spider在启动时进行爬取的url列表
    start_urls = [
        "http://news.ifeng.com/a/20170830/51804581_0.shtml",
        "http://news.ifeng.com/a/20170829/51801652_0.shtml"
    ]

    # start_request() 该方法必须返回一个可迭代对象 该对象包含了spider用于爬取的第一个request
    # 当spider启动爬取并且未制定URL时  该方法被调用 当指定了URL时  make_request_from_url()将被调用来创建Request对象
    # 该方法仅仅会被scrapy调用一次 因此您可以将其视为生成器
    #
    # 该方法的默认实现是使用的start_urls的url生成的Request
    #
    # 如果您想要爬取修改最初爬取某个网站的Request对象 您可以重写该方法

    # make_request_from_url(url)
    # 该方法接受一个URL并返回用于爬取的Request对象 该方法在初始化request时被start_request()调用 也被用于转化url为request

    # 默认未被复写的情况下 该方法的request对象中  parse()作为回调函数  dont_filer参数也被设置为开启


    # 当Reponse没有指定回调函数时  该方法是scrapy处理下载的Reponse的默认方法
    # parse负责处理response并返回处理的数据 以及跟进URL spider对其他的Request的回调函数也有相同的要求
    # 该方法以及其他的回调函数必须返回一个包含request及item的可迭代对象

    # 是spider的一个方法  在调用时  每个初始的url完成下载生成的response对象将会作为唯一的参数传递给该函数
    # 该方法负责解析返回的数据（response data）提取数据（生成item）以及生成需要进一步处理的url的request对象

    # log 使用scrapy.log.msg()方法记录log(message) log中自动带上改spider的name属性

    def parse(self,response):
        filename = response.url.split("/")[-2]
        with open(filename,'wb') as f:
            f.write(response.body)


# scrapy genspider mydomain spider的name 创建spider
# scrapy startproject tutorial 创建scrapy项目
# scrapy crawl demospider  启动spider

# spider类定义了如何爬取某个网站。包含了爬取的动作（是否跟进链接）以及如何从网页的内容中提取结构化数据（爬取item）
# 换句话说 spider就是您定义爬取的动作以及分析某个网页（或者事有些网页）的地方
#
# 对spider来说  爬取的循环类如下：

# 1，初始化的url初始化request,并设置回调函数，当request下载完毕并返回时，将生成Response，并作为参数传给该回调函数
# spider中初始的request是通过start_request()来获取的。start_request()读取start_urls中的url，并以parse为回调函数生成request

# 2,在回调函数内分析返回的网页内容，返回item对象或者request或者一个包括二者的可迭代容器。返回的request对象之后会经过scrapy处理
# 下载相应的内容，并调用设置的callback函数
#
# 3，在回调函数内 您可以使用选择器（selector）来分析网页的内容，并根据分析的数据生成item

# 4，最后 由spider返回的item将被存到数据库（由某些item pipeline处理）或者使用feed exports存到文件中


# Scrapy运行流程大概如下：
#
# 1,引擎从调度器中取出一个链接(URL)用于接下来的抓取
# 2,引擎把URL封装成一个请求(Request)传给下载器
# 3,下载器把资源下载下来，并封装成应答包(Response)
# 4,爬虫解析Response
# 5,解析出实体（Item）,则交给实体管道进行进一步的处理
# 6,解析出的是链接（URL）,则把URL交给调度器等待抓取















