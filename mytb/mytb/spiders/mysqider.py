# -*- coding: utf-8 -*-
import scrapy
import re,time,os,json
import requests
from mytb.items import MytbItem
from scrapy_splash import SplashRequest
from scrapy.http import Request

class MysqiderSpider(scrapy.Spider):
    name = 'mysqider'
    setoff = 1
    allowed_domains = ['s.taobao.com','item.taobao.com','detailskip.taobao.com']



    start_urls = ['https://s.taobao.com/list?q=%E7%8B%97%E7%B2%AE&style=grid&seller_type=taobao&sort=renqi-desc&cat=56470026']

    # def start_requests(self):
    #     for url in self.start_urls:
    #         yield SplashRequest(url, self.parse, args={'wait': '2'})

    def parse(self, response):
        body = response.body.decode('utf-8','ignore')
        allid = re.compile('"nid":"(.*?)"').findall(body)
        allbid = re.compile('"user_id":"(.*?)"').findall(body)



        for j in range(0,len(allid)):
            thisid = allid[j]
            thisbid = allbid[j]

            url = "https://item.taobao.com/item.htm?id="+str(thisid)
            # yield SplashRequest(url,self.next,args={'wait': 0.5})
            yield Request(url=url,callback=self.next,meta={"Sid":thisid,"Bid":thisbid,"url":url})


    def next(self,response):
        jsurl = "https://detailskip.taobao.com/service/getData/1/p1/item/detail/sib.htm?itemId={0}&sellerId={1}&modules=dynStock,qrcode,viewer,price,duty,xmpPromotion,delivery,activity,fqg,zjys,couponActivity,soldQuantity,originalPrice,tradeContract&callback=onSibRequestSuccess".format(response.meta["Sid"],response.meta["Bid"])
        reques = requests.get(url=jsurl,
                              headers={"user-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
                                       "referer": response.meta["url"]})



        item = MytbItem()
        try:

            item["price"] = re.compile('"promotion".*?price":"(.*?)"').findall(reques.text)[0]
        except Exception as e:
            item["price"] = "无"

            # print(item["price"])
        item["title"] = response.css(".tb-main-title::attr(data-title)").extract()[0]

        item["oldPrice"] = response.css(".tb-rmb-num::text").extract()[0]

        item["images"] = "http" + response.css("#J_ImgBooth ::attr(src)").extract()[0]

        item['dataurl'] = response.url





        for i in response.css(".attributes-list li::text").extract():
            alllist = i.split(":")
            list = alllist[0]
            data = alllist[1].strip()

            if list == "原产地":

                item["address"] = data

            elif list == "品牌":

                item["brand"] = data

            elif list == "品名":

                item["ProductName"] = data

            elif list == "生产厂家名称":

                item["ManufacturerName"] = data

            elif list == "生产厂家地址":

                item["ManufacturerAddress"] = data

            elif list == "适用犬种":

                item["Suitable"] = data

            elif list == "重量(g)":

                item["g"] = data+'g'

            elif list == "狗狗品种":

                item["Varieties"] = data

            elif list == "适用阶段":

                item["stage"] = data

            elif list == "食品口味":

                item["Flavor"] = data

            # elif list == "剩余保质期":
            #     item[""] = data
            # elif list == "宠物体型":
            #     item[""] = data
            elif list == "分类":

                item["Classification"] = data


        print(item)
        yield item
        if self.setoff < 100:
            self.setoff += 1
            url = "https://s.taobao.com/list?q=%E7%8B%97%E7%B2%AE&style=grid&seller_type=taobao&sort=renqi-desc&cat=56470026&s={}".format(self.setoff*60)
            yield Request(url=url,callback=self.parse)







