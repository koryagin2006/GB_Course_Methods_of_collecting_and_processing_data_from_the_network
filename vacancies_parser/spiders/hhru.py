# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse


class HhruSpider(scrapy.Spider):
    name = 'hhru'
    allowed_domains = ['hh.ru']
    start_urls = ['https://hh.ru/search/vacancy?area=1&st=searchVacancy&text=Python']

    def parse(self, response: HtmlResponse):
        next_page = response.xpath(
            "//a[@class='bloko-button HH-Pager-Controls-Next HH-Pager-Control']/@href").extract_first()
        if next_page is None:
            yield
        yield response.follow(next_page, callback=self.parse)

        vacancy_list = response.xpath("//a[@class='bloko-link HH-LinkModifier']/@href").extract()

        for link in vacancy_list:
            yield response.follow(link, callback=self.vacancy_parse)

    def vacancy_parse(self, response: HtmlResponse):
        vacancy_name = ''.join(response.xpath("//h1[@class='bloko-header-1']/text()").extract())
        vacancy_link = response.url
        company = ''.join(response.xpath("//span[@class='bloko-section-header-2 bloko-section-header-2_lite']/text()").extract())
        vacancy_info_json = ''.join(response.xpath("//script[@data-name='HH/GoogleDfpService']/@data-params").extract())
        location = ''.join(response.xpath("//div[@class='vacancy-company vacancy-company_with-logo']//p/span[1]/text()").extract())

        print(vacancy_name, vacancy_link, company, location)
        yield VacanciesParserItem(
            vacancy_name=vacancy_name,
            vacancy_link=vacancy_link,
            company=company,
            vacancy_info_json=vacancy_info_json,
            location=location
        )

