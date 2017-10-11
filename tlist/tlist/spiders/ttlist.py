# -*- coding: utf-8 -*-
import scrapy
import json
import re
from scrapy_splash import SplashRequest
import time,sys,os

from ..items import TlistItem,DefaultItemLoader
from scrapy.contrib.loader import ItemLoader
sys.stdout=open('pp.txt','w') #将打印信息输出在相应的位置下
class TtlistSpider(scrapy.Spider):
    name = 'ttlist'
    idnumber = 0
    allowed_domains = ['taobao.com']
    setoff = 0
    query = {
        'price':'.//div[@class="price g_price g_price-highlight"]/strong/text()',
        'images':'.//div[@class="pic"]/a/img/@data-src',
        'g':'.//span[@class="icon-pit icon-service-duliang"]/b/text()',
        'address':'.//div[@class="row row-3 g-clearfix"]/div[@class="location"]/text()',
        'title':'.//div[@class="pic"]/a/img/@alt',
        'userid':'.//div[@class="shop"]/a/@data-userid',
        'nid':'.//div[@class="row row-2 title"]/a/@data-nid',
        'shoping':'.//div[@class="shop"]/a/span[2]/text()'
    }
    url = 'https://s.taobao.com/list?spm=a21bo.50862.201867-links-9.35.223e1536mxzeI4&q=%E7%8B%97%E7%B2%AE&style=grid&seller_type=taobao&sort=renqi-desc&cps=yes&cat=56470026&bcoffset=12&s='
    start_urls = [url+str(setoff)]

    def start_requests(self):
        for i in self.start_urls:
            yield SplashRequest(i, self.parse_data, args={'wait': 0.5})


    # link_extractor = {
    # 记录符合的链接
    #     'image':SgmlLinkExtractor('')
    # }

    def parse_data(self, response):

        ti = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        PATH_STORE = "/home/wang/文档/"
        folder_path = PATH_STORE+ti



        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        with open("{0}/{1}.html".format(folder_path,self.idnumber),"w")as f:
            self.idnumber += 1
            f.write(response.text)



        # for i in response.xpath('//div[@class="item J_MouserOnverReq  "]'):
        #     item = TlistItem()
        #
        #     item['price'] = i.xpath(self.query['price']).extract()[0]
        #     item['images'] = 'http:'+i.xpath(self.query['images']).extract()[0]
        #     item['g'] = i.xpath(self.query['g']).extract()[0]+'/500g'
        #     item['address'] = i.xpath(self.query['address']).extract()[0]
        #     item['title'] = i.xpath(self.query['title']).extract()[0]
        #     item['userid'] = i.xpath(self.query['userid']).extract()[0]
        #     item['nid'] = i.xpath(self.query['nid']).extract()[0]
        #     item['shoping'] = i.xpath(self.query['shoping']).extract()[0]
        #
        #
        #     yield item
        if self.setoff < 600:
            self.setoff +=  60

            yield SplashRequest(self.url+str(self.setoff), self.parse_data, args={'wait': 0.5})









                # etaoItem_loader = DefaultItemLoader(item=TlistItem(),selector=response)
            #
            #
            # etaoItem_loader.add_xpath('price',self.query['price'])
            # etaoItem_loader.add_xpath('images',self.query['images'])
            # etaoItem_loader.add_xpath('g', self.query['g'])
            # etaoItem_loader.add_xpath('address', self.query['address'])
            # etaoItem_loader.add_xpath('title', self.query['title'])
            # etaoItem_loader.add_xpath('userid', self.query['userid'])
            # etaoItem_loader.add_xpath('nid', self.query['nid'])
            # etaoItem_loader.add_xpath('shoping', self.query['shoping'])
            #
            # e_item = etaoItem_loader.load_item()
            # print(e_item)
        #     yield item

        #




