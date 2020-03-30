from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from vacancies_parser import settings
from _Scrapy_projects.project_2_vacancies.vacancies_parser.spiders.hhru import HhruSpider
from _Scrapy_projects.project_2_vacancies.vacancies_parser.spiders.sjru import SjruSpider


if __name__ == '__main__':
    search_input = input('Please enter the search: ')
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)
    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(HhruSpider, search=search_input)
    process.crawl(SjruSpider, search=search_input)
    process.start()