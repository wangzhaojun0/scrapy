# -*- coding: utf-8 -*-

# Define your item pipelines here
#./
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.conf import settings
import pymongo
import time

class MytbPipeline(object):
    def __init__(self):
        host = settings["MONGODB_HOST"]
        port = settings["MONGODB_PORT"]
        dbname = settings["MONGODB_DBNAME"]
        sheetname = time.strftime('%Y-%m-%d', time.localtime(time.time()))

        # 创建MONGODB数据库链接
        client = pymongo.MongoClient(host=host, port=port)
        # 指定数据库
        mydb = client[dbname]
        # 存放数据的数据库表名
        self.sheet = mydb[sheetname]
        # self.ti =
        # self.dog = {self.ti: []}

    def process_item(self, item, spider):
        self.sheet.insert(dict(item))
        # self.dog[self.ti].append(dict(item))
        return item

    # def close_spider(self, spider):
    #     self.sheet.insert(self.dog)
