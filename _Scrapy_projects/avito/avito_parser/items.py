# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst


def cleaner_photo(value):
    if values[:2] == '//':
        return f'http:{value}'
    return value

class AvitoParserItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    photos = scrapy.Field()
