# -*- coding: utf-8 -*-
import scrapy


class LeroymerlinSpider(scrapy.Spider):
    name = 'leroymerlin'
    allowed_domains = ['leroymerlin.ru']
    start_urls = ['https://orenburg.leroymerlin.ru/catalogue/dreli-shurupoverty/']

    def parse(self, response):
        pass
