# -*- coding: utf-8 -*-
# Item Loaders
#
# Item Loaders 提供了一种简便的构件（mechanism）来抓取:ref:Items<topics-items>.
# 虽然Items可以从它自己的类似字典（dictionary-like）的API得到所需信息 ,
# 不过 Item Loaders提供了许多更加方便的API，这些API通过自动完成那些具有共通性的任务，
# 可从抓取进程中得到这些信息, 比如预先解析提取到的原生数据。 换句话来解释,
# Items 提供了盛装抓取到的数据的*容器* , 而Item Loaders提供了构件*装载populating*该容器。

# 要使用Item Loader, 你必须先将它实例化. 你可以使用类似字典的对象(例如: Item or dict)来进行实例化,
# 或者不使用对象也可以, 当不用对象进行实例化的时候,Item会自动使用 ItemLoader.default_item_class
# 属性中指定的Item 类在Item Loader constructor中实例化.

# 然后,你开始收集数值到Item Loader时,通常使用 Selectors. 你可以在同一个item field 里面添加多个数值;
# Item Loader将知道如何用合适的处理函数来“添加”这些数值.
from scrapy.loader import ItemLoader


class Product(object):
    pass


def parse(self,response):
    l = ItemLoader(item=Product(),response=response)
    l.add_xpath('name','//div[@class="product_name"]')
    l.add_xpath('name', '//div[@class="product_title"]')
    l.add_xpath('price', '//p[@id="price"]')
    l.add_css('stock', 'p#stock]')
    l.add_value('last_updated', 'today')
    return l.load_item()


# 换言之,数据通过用 add_xpath() 的方法,把从两个不同的XPath位置提取的数据收集起来. 这是将在以后分配给 name 字段中的数据｡
#
# 之后,类似的请求被用于 price 和 stock 字段 (后者使用 CSS selector 和 add_css() 方法), 最后使用不同的方法 add_value() 对 last_update 填充文本值( today ).
#
# 最终, 当所有数据被收集起来之后, 调用 ItemLoader.load_item() 方法, 实际上填充并且返回了之前通过调用 add_xpath(), add_css(), and add_value() 所提取和收集到的数据的Item.

