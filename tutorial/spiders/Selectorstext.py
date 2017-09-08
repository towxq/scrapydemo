# -*- coding: utf-8 -*-

from scrapy.selector import Selector
from scrapy.http import HtmlResponse


body = '<html><body><span>good</span></body></html>'
print Selector(text=body).xpath('//span/text()').extract()

response = HtmlResponse(url='http://www.ifeng.com/', body=body)
print Selector(response=response).xpath('//span/text()').extract()





# 选择器(Selectors)
#
# Scrapy提取数据有自己的一套机制。它们被称作选择器(seletors)，
# 因为他们通过特定的 XPath 或者 CSS 表达式来“选择” HTML文件中的某个部分。
#
# 构造选择器(selectors)
#
# Scrapy selector是以 文字(text) 或 TextResponse 构造的 Selector 实例。 其根据输入的类型自动选择最优的分析方法(XML vs HTML):

# scrapy shell http://news.ifeng.com/a/20170905/51873424_0.shtml
#
# response.xpath('//title/text()').extract()

# .xpath() 及 .css() 方法返回一个类 SelectorList 的实例
#
# .extract() 读取原文内容

# 嵌套选择器(selectors)
# 选择器方法( .xpath() or .css() )返回相同类型的选择器列表，因此你也可以对这些选择器调用选择器方法
#
# 结合正则表达式使用选择器(selectors)
# Selector 也有一个 .re() 方法，用来通过正则表达式来提取数据。然而，不同于使用 .xpath() 或者 .css() 方法,
# .re() 方法返回unicode字符串的列表。所以你无法构造嵌套式的 .re() 调用

# 内建选择器的参考
#
# Selector 的实例是对选择某些内容响应的封装。
# response 是 HtmlResponse 或 XmlResponse 的一个对象，将被用来选择和提取数据。
#
# text 是在 response 不可用时的一个unicode字符串或utf-8编码的文字。将 text 和 response 一起使用是未定义行为。
#
# type 定义了选择器类型，可以是 "html", "xml" or None (默认).
#
# 如果 type 是 None ，选择器会根据 response 类型(参见下面)自动选择最佳的类型，或者在和 text 一起使用时，默认为 "html" 。
#
# 如果 type 是 None ，并传递了一个 response ，选择器类型将从response类型中推导如下：
#
# "html" for HtmlResponse type
# "xml" for XmlResponse type
# "html" for anything else
# 其他情况下，如果设定了 type ，选择器类型将被强制设定，而不进行检测。
#
# xpath(query)
# 寻找可以匹配xpath query 的节点，并返回 SelectorList 的一个实例结果，单一化其所有元素。列表元素也实现了 Selector 的接口。
#
# query 是包含XPATH查询请求的字符串。

# css(query)
# 应用给定的CSS选择器，返回 SelectorList 的一个实例。
#
# query 是一个包含CSS选择器的字符串。
#
# 在后台，通过 cssselect 库和运行 .xpath() 方法，CSS查询会被转换为XPath查询。
#
#
# extract()
# 串行化并将匹配到的节点返回一个unicode字符串列表。 结尾是编码内容的百分比。
#
#
# re(regex)
# 应用给定的regex，并返回匹配到的unicode字符串列表。、
#
# regex 可以是一个已编译的正则表达式，也可以是一个将被 re.compile(regex) 编译为正则表达式的字符串。
#
# register_namespace(prefix, uri)
# 注册给定的命名空间，其将在 Selector 中使用。 不注册命名空间，你将无法从非标准命名空间中选择或提取数据。参见下面的例子。
#
# remove_namespaces()
# 移除所有的命名空间，允许使用少量的命名空间xpaths遍历文档。参加下面的例子。
#
# __nonzero__()
# 如果选择了任意的真实文档，将返回 True ，否则返回 False 。 也就是说， Selector 的布尔值是通过它选择的内容确定的。
#
#
# SelectorList对象
#
#
# SelectorList 类是内建 list 类的子类，提供了一些额外的方法。
# xpath(query)
# 对列表中的每个元素调用 .xpath() 方法，返回结果为另一个单一化的 SelectorList 。
#
# query 和 Selector.xpath() 中的参数相同。
#
# css(query)
# 对列表中的各个元素调用 .css() 方法，返回结果为另一个单一化的 SelectorList 。
#
# query 和 Selector.css() 中的参数相同。
#
# extract()
# 对列表中的各个元素调用 .extract() 方法，返回结果为单一化的unicode字符串列表。
#
# re()
# 对列表中的各个元素调用 .re() 方法，返回结果为单一化的unicode字符串列表。
#
# __nonzero__()
# 列表非空则返回True，否则返回False。
