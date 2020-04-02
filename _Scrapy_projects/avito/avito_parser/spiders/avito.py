# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse
from avito_parser.items import AvitoParserItem


class AvitoSpider(scrapy.Spider):
    name = 'avito'
    allowed_domains = ['avito.ru']

    # start_urls = ['-']

    def __init__(self, search):
        self.start_urls = [f'https://www.avito.ru/moskva?q={search}']

    def parse(self, response: HtmlResponse):
        ads_links = response.xpath("//div[@class='snippet-title-row']//a/@href").extract()
        for link in ads_links:
            yield response.follow(link, callback=self.parse_ads)

    def parse_ads(self, response: HtmlResponse):
        photos = response.xpath("//div[@class='gallery-img-wrapper js-gallery-img-wrapper']/div/@data-url").extract()
        name = response.xpath("//span[@class='title-info-title-text']/text()").extract_first()
        print(name, photos)
        yield AvitoParserItem(name=name, photos=photos)
