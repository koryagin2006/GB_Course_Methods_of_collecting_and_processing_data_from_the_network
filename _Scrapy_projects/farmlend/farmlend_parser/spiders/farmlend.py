# -*- coding: utf-8 -*-
import scrapy


class FarmlendSpider(scrapy.Spider):
    name = 'farmlend'
    allowed_domains = ['farmlend.ru']
    start_urls = ['http://farmlend.ru/']

    def parse(self, response):
        pass
