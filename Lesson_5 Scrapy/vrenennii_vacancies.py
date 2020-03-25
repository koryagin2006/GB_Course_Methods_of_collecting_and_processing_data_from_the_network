import requests
from lxml import html
import json

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/80.0.3987.149 Safari/537.36 '}

response = requests.get('https://hh.ru/vacancy/36396758?query=Python', headers=header).text
response = html.fromstring(response)

vacancy_name = response.xpath("//h1[@class='bloko-header-1']/text()")[0]
company = ''.join(response.xpath("//span[@class='bloko-section-header-2 bloko-section-header-2_lite']/text()"))
vacancy_info_json = ''.join(response.xpath("//script[@data-name='HH/GoogleDfpService']/@data-params"))
location = ''.join(response.xpath("//div[@class='vacancy-company vacancy-company_with-logo']//p/span[1]/text()"))


# salary_min = json.loads(vacancy_info_json)['vac_salary_from']
# salary_max = json.loads(vacancy_info_json)['vac_salary_to']
# currency = json.loads(vacancy_info_json)['vac_salary_cur']

for i in [vacancy_name, company, location]:
    print(i, '\n')
