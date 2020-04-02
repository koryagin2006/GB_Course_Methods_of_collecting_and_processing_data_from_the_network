from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

"""
1) Взять любую категорию товаров на сайте леруа мерлен (https://leroymerlin.ru/catalogue/). 
   И собрать с использованием ItemLoader следующие данные:
    - Название
    - Все фото
    - Параметры товара в объявлении
2) С использованием output_processor и input_processor реализовать очистку и преобразование данных. 
Значения цен должны быть в виде числового значения.
"""

from leroymerlin_parser.spiders.leroymerlin import LeroymerlinSpider
from leroymerlin_parser import settings

if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)
    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(LeroymerlinSpider)
    process.start()
