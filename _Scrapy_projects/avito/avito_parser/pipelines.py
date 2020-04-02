# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.pipelines.images import ImagesPipeline


class DataBasePipeline(object):
    def process_item(self, item, spider):
        return item


class AvitoPhotosPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        if item['photos']:
            for img in item['photos']:
                try:
                    yield scrapy.Request(f'http:{img}')
                except TypeError as e:
                    print(e)

    def item_completed(self, results, item, info):
        if results:
            pass
        return item
