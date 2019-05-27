# -*- coding: utf-8 -*-
import scrapy
from items import ImageItem

class SsSpider(scrapy.Spider):
    name = 'ss'
    start_urls = ['https://my.ss8.fun/', 'https://ttizi.com/', 'https://d.ishadowx.com/']

    def parse(self, response):
            if response.url == 'https://my.ss8.fun/':
                return scrapy.Request(response.url,callback=self.parse_ss8)
            elif response.url == 'https://ttizi.com/':
                return scrapy.Request(response.url,callback=self.parse_ttizi)
            elif response.url == 'https://d.ishadowx.com/':
                return scrapy.Request(response.url,callback=self.parse_ishadow)


    def parse_ttizi(self,response):
        html = response.css('.card-body')
        for data in html:
            item = ImageItem()
            item['url'] = data.css('a:nth-child(2)::attr(href)').extract_first()
            yield item

    def parse_ishadow(self,response):
        html = response.css('.hover-text')
        for data in html:
            item = ImageItem()
            try:
                item['url'] = 'https://d.ishadowx.com/'+data.css('h4 a::attr(href)').extract_first()
                yield item
            except:
                continue

    def parse_ss8(self,response):
        html = response.css('article')
        for data in html:
            item = ImageItem()
            item['url'] = 'https://my.ss8.fun/'+data.css('a::attr(href)').extract_first()
            yield item

    # def start_requests(self):
    #     urllist = ['https://lncn.org/','https://ttizi.com/','https://d.ishadowx.com/']
    #     for url in urllist:
    #         yield scrapy.Request(url,callback=self.distinct)
            # if url == 'https://lncn.org/':
            #     return scrapy.Request(url,callback=self.parse_lncn)
            # elif url == 'https://ttizi.com/':
            #     return scrapy.Request(url,callback=self.parse_ttizi)
            # elif url == 'https://d.ishadowx.com/':
            #     return scrapy.Request(url,callback=self.parse_ishadow)
