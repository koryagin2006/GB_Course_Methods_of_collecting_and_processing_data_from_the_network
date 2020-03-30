from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from z_avito.z_avito_parser import settings
from z_avito.z_avito_parser.spiders.avito import AvitoSpider

if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)
    process = CrawlerProcess(settings=crawler_settings)
    # input()
    process.crawl(AvitoSpider, search='диван')
    process.start()