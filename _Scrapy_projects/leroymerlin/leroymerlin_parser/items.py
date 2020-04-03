# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst


def cleaner_price(value):
    value = value.replace(' ', '')
    value = int(value)

def cleaner_vendor_code(value):
    value = int(value)


class LeroymerlinParserItem(scrapy.Item):
    # define the fields for your item here like:
    _id = scrapy.Field()
    name = scrapy.Field(output_processor=TakeFirst())
    description = scrapy.Field(output_processor=TakeFirst())
    photos = scrapy.Field()
    vendor_code = scrapy.Field(input_processor=MapCompose(cleaner_vendor_code))
    price = scrapy.Field(input_processor=MapCompose(cleaner_price))
