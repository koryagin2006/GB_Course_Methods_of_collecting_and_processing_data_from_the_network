# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse


class AvitoSpider(scrapy.Spider):
    name = 'avito'
    allowed_domains = ['avito.ru']
    # start_urls = ['https://www.avito.ru/orenburg/kvartiry/prodam-ASgBAgICAUSSA8YQ?cd=1']

    def __init__(self, search):
        self.start_urls = [f'https://www.avito.ru/rossiya?q={search}']

    def parse(self, response: HtmlResponse):
        ads_link = response.xpath("//h3[@class='snippet-title']/a/@href").extract()
        for link in ads_link:
            yield response.follow(link, callback=self.parse_ads())

    def parse_ads(self, response: HtmlResponse):
        photos = response.xpath("//div[@class='gallery-img-wrapper js-gallery-img-wrapper']//div["
                                "@class='gallery-img-frame js-gallery-img-frame']/@data-url").extract()
        name = response.xpath("//span[@class='title-info-title-text']/text()").extract_first()
        print(name, photos)
