# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse
from avito_parser.items import AvitoParserItem
from scrapy.loader import ItemLoader

class AvitoSpider(scrapy.Spider):
    name = 'avito'
    allowed_domains = ['avito.ru']
    # start_urls = ['http://avito.ru/']
    def __init__(self, search):
        self.start_urls = [f'https://www.avito.ru/rossiya?q={search}']


    def parse(self, response):
        ads_links = response.xpath('//a[@class="snippet-link js-snippet-link"]/@href').extract()
        for link in ads_links:
            yield response.follow(link, callback=self.parse_ads)

    def parse_ads(self, response: HtmlResponse):
        photos = response.xpath('//div[contains(@class, "gallery-img-wrapper")]//div[contains(@class, "gallery-img-frame")]/@data-url').extract()
        name = response.css('h1.title-info-title span.title-info-title-text::text').extract_first()
        print(name, photos)

