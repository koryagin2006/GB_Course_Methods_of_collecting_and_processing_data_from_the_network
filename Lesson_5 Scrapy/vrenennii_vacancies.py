import requests
from lxml import html

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/80.0.3987.149 Safari/537.36 '}

response = requests.get('https://hh.ru/vacancy/36396758?query=Python', headers=header).text
response = html.fromstring(response)

vacancy_name = response.xpath("//h1[@class='bloko-header-1']/text()")[0]
company = ''.join(response.xpath("//span[@class='bloko-section-header-2 bloko-section-header-2_lite']/text()"))
salary = response.xpath("//div[@class='supernova-footer']/@data-params")


for i in [vacancy_name, company, salary]:
    print(i, '\n')