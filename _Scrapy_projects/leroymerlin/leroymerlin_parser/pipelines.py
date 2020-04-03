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
        return item
