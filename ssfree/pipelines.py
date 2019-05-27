# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline

class SsfreePipeline(object):
    def process_item(self, item, spider):
        return item

class ImagePipeline(ImagesPipeline): # 保存图片的方法重写
    def file_path(self, request, response=None, info=None):
        # 保存的文件名
        url = request.url
        file_name = url.split('/')[-1]+'.png'
        return file_name

    def item_completed(self, results, item, info):
        # 一旦一张图片下载完成就执行的操作
        image_paths = [x['path'] for ok ,x in results if ok]
        if not image_paths:
            raise DropItem('image download failed')
        return item

    def get_media_requests(self, item, info):
        #  用于返回要处理的request请求
        yield Request(item['url'])