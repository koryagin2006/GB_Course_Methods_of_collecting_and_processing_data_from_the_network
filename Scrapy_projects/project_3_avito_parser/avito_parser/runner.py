from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from _Scrapy_projects.project_3_avito_parser.avito_parser.spiders.avito import AvitoSpider
from _Scrapy_projects.project_3_avito_parser.avito_parser import settings

if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)
    process = CrawlerProcess(settings=crawler_settings)
    # input()
    process.crawl(AvitoSpider, search='диван')
    process.start()
