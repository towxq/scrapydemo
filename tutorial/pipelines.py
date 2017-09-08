# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json


class TutorialPipeline(object):
    def process_item(self, item, spider):
        return item


class SfbestPipeline(object):
    def process_item(self, item, spider):
        # for items in item.keys():
        # #     for ii in item[items]:
        #         str = ii.encode('utf-8')
        #         with open("sfbest.txt",'a') as f:
        #             f.write(str.strip())
        # print type(item)
        self.file = codecs.open('sfbest_data.json', mode='wb', encoding='utf-8')
        line = json.dumps(dict(item)).strip() + '\n'
        self.file.write(line.decode("unicode_escape"))
# 项目中的pipelines文件