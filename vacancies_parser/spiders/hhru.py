# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse


class HhruSpider(scrapy.Spider):
    name = 'hhru'
    allowed_domains = ['hh.ru']
    start_urls = ['https://hh.ru/search/vacancy?area=1&st=searchVacancy&text=Python']

    def parse(self, response: HtmlResponse):
        next_page = response.xpath("//a[@class='bloko-button HH-Pager-Controls-Next HH-Pager-Control']").extract_first()
        if next_page is None:
            yield
        yield response.follow(next_page, callback=self.parse)

        vacancy_list = response.xpath("//a[@class='bloko-link HH-LinkModifier']/@href").extract()

        for link in vacancy_list:
            yield response.follow(link, callback=self.vacancy_parse)

    def vacancy_parse(self, response: HtmlResponse):
        name = response.xpath("//h1[@class='bloko-header-1']/text()").extract()
        salary = response.xpath("//span[@class='bloko-header-2 bloko-header-2_lite']/text()").extract()
        print(name, salary)
