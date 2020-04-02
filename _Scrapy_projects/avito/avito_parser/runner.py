from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from avito_parser.spiders.avito import AvitoSpider
from avito_parser import settings

if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)
    process = CrawlerProcess(settings=crawler_settings)
    # search_input = input('Please enter search: ')
    search_input = 'квартира'
    process.crawl(AvitoSpider, search=search_input)
    process.start()
