# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest
import re,os,time
from scrapy.http import Request

class SpiderhtmlSpider(scrapy.Spider):
    name = 'spiderhtml'
    allowed_domains = ['item.taobao.com',"s.taobao.com"]
    setoff = 1
    datatime = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    if not os.path.exists("/home/wang/mytb/html/" + time.strftime('%Y-%m-%d', time.localtime(time.time()))):
        os.mkdir("/home/wang/mytb/html/" + time.strftime('%Y-%m-%d', time.localtime(time.time())))

    start_urls = ['https://s.taobao.com/list?q=%E7%8B%97%E7%B2%AE&style=grid&seller_type=taobao&sort=renqi-desc&cat=56470026']

    def parse(self, response):
        body = response.body.decode('utf-8','ignore')
        allid = re.compile('"nid":"(.*?)"').findall(body)
        allbid = re.compile('"user_id":"(.*?)"').findall(body)



        for j in range(0,len(allid)):
            thisid = allid[j]
            thisbid = allbid[j]

            url = "https://item.taobao.com/item.htm?id="+str(thisid)
            yield SplashRequest(url,self.next,args={'wait': 0.5})
    def next(self,response):

        with open("/home/wang/mytb/html/"+time.strftime('%Y-%m-%d', time.localtime(time.time()))+"/"+self.datatime+".html","wb") as fb:
                fb.write(response.text)

        if self.setoff < 100:
            self.setoff += 1
            url = "https://s.taobao.com/list?q=%E7%8B%97%E7%B2%AE&style=grid&seller_type=taobao&sort=renqi-desc&cat=56470026&s={}".format(
                self.setoff * 60)
            yield Request(url=url, callback=self.parse)

#


