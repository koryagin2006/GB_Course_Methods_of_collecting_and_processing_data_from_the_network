# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse
from leroymerlin_parser.items import LeroymerlinParserItem


class LeroymerlinSpider(scrapy.Spider):
    name = 'leroymerlin'
    allowed_domains = ['leroymerlin.ru']
    start_urls = ['https://orenburg.leroymerlin.ru/catalogue/dreli-shurupoverty/']

    def parse(self, response: HtmlResponse):
        next_page = response.xpath(
            "//a[@class='paginator-button next-paginator-button']").extract_first()
        if next_page is None:
            yield
        yield response.follow(next_page, callback=self.parse)

        product_links = response.xpath("//div[@class='product-name']/a/@href").extract()
        for link in product_links:
            yield response.follow(link, callback=self.parse_product)
            # print(link)
    def parse_product(self, response: HtmlResponse):
        name = response.xpath("//h1[@class='header-2']/text()").extract_first()
        description = response.xpath("//section[@id='nav-description']//div/p/text()").extract()
        photos = response.xpath("//img[@alt='product image']/@src").extract()

        print(name, photos,description)
        # yield AvitoParserItem(name=name, photos=photos, description=description)
