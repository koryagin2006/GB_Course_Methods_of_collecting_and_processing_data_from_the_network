# -*- coding: utf-8 -*-
import scrapy


class AvitoSpider(scrapy.Spider):
    name = 'avito'
    allowed_domains = ['aviro.ru']
    start_urls = ['http://aviro.ru/']

    def parse(self, response):
        pass
