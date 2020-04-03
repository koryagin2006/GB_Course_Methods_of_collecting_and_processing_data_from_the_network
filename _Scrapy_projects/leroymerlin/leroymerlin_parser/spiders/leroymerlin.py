# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse
from scrapy.loader import ItemLoader

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
        loader = ItemLoader(item=LeroymerlinParserItem(), response=response)

        loader.add_xpath('name', "//h1[@class='header-2']/text()")
        loader.add_xpath('description', "//section[@id='nav-description']//div/p/text()")
        loader.add_xpath('photos', "//img[@alt='product image']/@src")
        loader.add_xpath('vendor_code', "//span[@slot='article']/@content")
        loader.add_xpath('price', "//span[@slot='price']/text()")

        yield loader.load_item()
