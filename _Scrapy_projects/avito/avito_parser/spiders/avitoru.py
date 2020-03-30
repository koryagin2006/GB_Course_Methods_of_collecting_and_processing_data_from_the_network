# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse


class AvitoruSpider(scrapy.Spider):
    name = 'avitoru'
    allowed_domains = ['avito.ru']
    start_urls = ['https://www.avito.ru/rossiya/kvartiry']

    def __init__(self, response: HtmlResponse):
        start_urls = [f'https://www.avito.ru/rossiya?q={search}']

    def parse(self, response):
        ads_list = response.xpath("//a[@class='snippet-link']/@href").extract()
        for link in ads_list:
            yield response.follow(link, callback=self.parse_ads)

    def parse_ads(self, response: HtmlResponse):
        photos = response.xpath("//div[@class='gallery-img-wrapper js-gallery-img-wrapper']/div[1]/@data-url").extract()
        name = response.xpath("//span[@class='title-info-title-text']/text()").extract_first()

        print(name, photos)
