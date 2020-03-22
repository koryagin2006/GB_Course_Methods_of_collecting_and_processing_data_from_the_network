# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse


class HhruSpider(scrapy.Spider):
    name = 'hhru'
    allowed_domains = ['hh.ru']
    start_urls = ['https://orenburg.hh.ru/search/vacancy?L_save_area=true&clusters=true&enable_snippets=true&text'
                  '=Python&showClusters=true']

    def parse(self, response: HtmlResponse):
        next_page = response.xpath(
            "//a[@class='bloko-button HH-Pager-Controls-Next HH-Pager-Control']/@href").extract_first()
        yield response.follow(next_page, callback=self.parse)
        vacancy_list = response.xpath("//a[@class='bloko-link HH-LinkModifier']/@href").extract()
        for link in vacancy_list:
            yield response.follow(link, callback=self.vacancy_parse)

    def vacancy_parse(self, response:HtmlResponse):
        vac_name = response.xpath("//h1[@class='bloko-header-1']/text()")
        vac_link = response.url
        vac_salary = tree.xpath("//span[@class='bloko-header-2 bloko-header-2_lite']/text()")
        print(
            vac_name,'\n',
            vac_link,'\n',
            vac_salary
        )