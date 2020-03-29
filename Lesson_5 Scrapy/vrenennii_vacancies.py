from pprint import pprint
import requests
from lxml import html
import json

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/80.0.3987.149 Safari/537.36 '}

response = requests.get('https://russia.superjob.ru/vakansii/sistemnyj-analitik-33619990.html', headers=header).text
# response = requests.get('https://hh.ru/vacancy/36396758?query=Python', headers=header).text
response = html.fromstring(response)

# vacancy_list = response.xpath("//div[@class='_3zucV _2GPIV f-test-vacancy-item i6-sc _3VcZr']//div[@class='_2g1F-']/a/@href")
# for i in vacancy_list:
#     print(i)

vacancy_name = response.xpath("//h1[@class='_3mfro rFbjy s1nFK _2JVkc']/text()")[0]
company = ''.join(response.xpath("//h2[@class='_3mfro PlM3e _2JVkc _2VHxz _3LJqf _15msI']/text()"))
vacancy_info_json = json.loads(response.xpath("//script[@type='application/ld+json']/text()")[1])
location = ''.join(response.xpath("//span[@class='_6-z9f']//span[@class='_3mfro _1hP6a _2JVkc']/text()"))

pprint(vacancy_info_json)
# salary_min = salary['value']['minValue']
# salary_max = salary['value']['maxValue']
# currency = salary['currency']
#
# for i in [salary_min, salary_max, currency]:
#     print(i)

# for i in [vacancy_name, company, location]:
#     print(i, '\n')
