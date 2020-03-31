# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse
from avito_parser.items import AvitoParserItem
from scrapy.loader import ItemLoader


class AvitoruSpider(scrapy.Spider):
    name = 'avitoru'
    allowed_domains = ['avito.ru']
    start_urls = ['https://www.avito.ru/rossiya?q=диван']

    def __init__(self, search):
        start_urls = [f'https://www.avito.ru/rossiya?q={search}']

    def parse(self, response):
        ads_list = response.xpath("//a[@class='snippet-link']/@href").extract()
        for link in ads_list:
            yield response.follow(link, callback=self.parse_ads)

    def parse_ads(self, response: HtmlResponse):
        # photos = response.xpath("//div[@class='gallery-img-wrapper js-gallery-img-wrapper']/div[1]/@data-url").extract()
        # name = response.xpath("//span[@class='title-info-title-text']/text()").extract_first()
        # yield AvitoParserItem(name=name, photos=photos)
        loader = ItemLoader(item=AvitoParserItem, response=response)
        loader.add_xpath('photos', "//div[@class='gallery-img-wrapper js-gallery-img-wrapper']/div[1]/@data-url")
        loader.add_xpath('name', "//span[@class='title-info-title-text']/text()")
        yield loader.load_item()