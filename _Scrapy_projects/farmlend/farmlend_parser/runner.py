from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from farmlend_parser import settings
from farmlend_parser.spiders.farmlend import FarmlendSpider

search_input = input('Please enter the search: ')

if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)
    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(FarmlendSpider, search=search_input)
    process.start()