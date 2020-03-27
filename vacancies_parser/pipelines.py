# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient

class VacanciesParserPipeline(object):
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.mongobase = client.vacansy_305

    def process_item(self, item, spider):
        collection = self.mongobase[spider.name]

        return item
