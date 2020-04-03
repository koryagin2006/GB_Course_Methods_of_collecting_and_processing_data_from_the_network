# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from pymongo import MongoClient
from scrapy.pipelines.images import ImagesPipeline


class DataBasePipeline(object):
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.mongo_base = client.leroymerlin

    def process_item(self, item, spider):
        # collection = self.mongo_base[spider.name]
        collection = self.mongo_base['dreli-shurupoverty']
        collection.insert_one(item)
        return item


class LeroymerlinParserPipeline(object):
    def process_item(self, item, spider):
        item['price'] = int(item['price'][0].replace(' ', ''))
        item['vendor_code'] = int(item['vendor_code'][0])
        return item


class LeroyPhotosPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        if item['photos']:
            for img in item['photos']:
                try:
                    yield scrapy.Request(img)
                except TypeError as e:
                    print(e)

    def item_completed(self, results, item, info):
        if results:
            item['photos'] = [itm[1] for itm in results if itm[0]]
        return item


class MyImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for image_url in item['photos']:
            yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        image_path = [x['path'] for ok, x in results if ok]
        if not image_path:
            raise DropItem("Item contains no images")
        item['image_path'] = image_path
        return item
