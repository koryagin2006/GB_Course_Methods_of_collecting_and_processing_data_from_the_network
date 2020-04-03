import requests
from pprint import pprint
from lxml import html
main_link = 'https://www.avito.ru/orenburg/kvartiry/3-k_kvartira_80_m_1417_et._1647076412'
response = requests.get(main_link).text
tree = html.fromstring(response)


params_list = tree.xpath("//li[@class='item-params-list-item']")

for param in params_list:
    name = param.xpath("./span/text()")[0]
    value = param.xpath("./text()")[1]
    print(name, value)
