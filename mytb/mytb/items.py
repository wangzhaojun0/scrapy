# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MytbItem(scrapy.Item):
       price = scrapy.Field()
       title = scrapy.Field()
       oldPrice = scrapy.Field()
       images = scrapy.Field()
       # 重量
       g = scrapy.Field()
       # 地址
       address = scrapy.Field()
       # 品牌
       brand = scrapy.Field()
       # 品名
       ProductName = scrapy.Field()
       #生产厂家名称
       ManufacturerName = scrapy.Field()
       # 生产厂家地址
       ManufacturerAddress = scrapy.Field()
       # 适用犬种
       Suitable = scrapy.Field()

       # 狗狗品种
       Varieties = scrapy.Field()
       # 适用阶段
       stage = scrapy.Field()
       # 食品口味
       Flavor = scrapy.Field()
       # 剩余保质期
       # 宠物体型
       # 分类
       Classification = scrapy.Field()
#        详情链接
       dataurl = scrapy.Field()


