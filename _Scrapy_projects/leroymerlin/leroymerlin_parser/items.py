# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst, Join, Identity


class LeroymerlinParserItem(scrapy.Item):
    # define the fields for your item here like:
    _id = scrapy.Field()
    name = scrapy.Field(output_processor=TakeFirst())
    description = scrapy.Field(output_processor=Join())
    photos = scrapy.Field()
    image_path = scrapy.Field()
    vendor_code = scrapy.Field()
    price = scrapy.Field()
