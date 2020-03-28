from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from vacancies_parser import settings
from vacancies_parser.spiders.hhru import HhruSpider
from vacancies_parser.spiders.sjru import SjruSpider

if __name__ == '__main__':
    search_query = 'Python'

    crawler_settings = Settings()
    crawler_settings.setmodule(settings)
    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(HhruSpider)
    # process.crawl(SjruSpider)
    process.start()