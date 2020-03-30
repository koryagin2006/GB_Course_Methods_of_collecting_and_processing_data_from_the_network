# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient


class VacanciesParserPipeline(object):
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.mongobase = client.vacansy_305

    def process_item(self, item, spider):
        collection = self.mongobase[spider.name]

        if spider.name == 'sjru':
            item['currency'] = item['vacancy_info_json']['baseSalary']['currency']
            try:
                item['salary_min'] = item['vacancy_info_json']['baseSalary']['value']['minValue']
            except KeyError:
                item['salary_min'] = None
            try:
                item['salary_max'] = item['vacancy_info_json']['baseSalary']['value']['maxValue']
            except KeyError:
                item['salary_max'] = None

        elif spider.name == 'hhru':
            if item['vacancy_info_json']['vac_salary_cur'] == '':
                item['currency'] = None
            elif item['vacancy_info_json']['vac_salary_cur'] == 'RUR':
                item['currency'] = 'RUB'
            else:
                item['currency'] = item['vacancy_info_json']['vac_salary_cur']

            if item['vacancy_info_json']['vac_salary_from'] == '':
                item['salary_min'] = None
            else:
                item['salary_min'] = int(item['vacancy_info_json']['vac_salary_from'])

            if item['vacancy_info_json']['vac_salary_to'] == '':
                item['salary_max'] = None
            else:
                item['salary_max'] = int(item['vacancy_info_json']['vac_salary_to'])

        collection.insert_one(item)
        return item
