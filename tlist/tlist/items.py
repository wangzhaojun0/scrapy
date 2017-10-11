# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import re
from scrapy.loader.processors import  TakeFirst,MapCompose,Join
from scrapy.loader import ItemLoader
class DefaultItemLoader(ItemLoader):
    #自定义itemloader，继承scrapy的ItemLoader类
    default_output_processor = TakeFirst()
def remove_splash(value):
    #去掉工作城市的斜线

    return value.replace("\n","").strip()
def get_value(value):
    return value
class TlistItem(scrapy.Item):
    price = scrapy.Field(
        # output_processor=MapCompose(get_value)
    )

    images = scrapy.Field()

    g = scrapy.Field()

    address = scrapy.Field()

    title = scrapy.Field(
        # input_processor=MapCompose(remove_splash),
    )

    userid = scrapy.Field()

    nid = scrapy.Field()

    shoping = scrapy.Field()