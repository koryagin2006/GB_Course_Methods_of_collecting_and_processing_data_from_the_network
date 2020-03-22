import requests
from lxml import html


User_Agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
header={'User-Agent': User_Agent}

response = requests.get("https://orenburg.hh.ru/vacancy/35758988?query=Python", headers=header).text
tree = html.fromstring(response)

name = tree.xpath("//h1[@class='bloko-header-1']/text()")
vac_salary = tree.xpath("//span[@class='bloko-header-2 bloko-header-2_lite']/text()")

print(
    name,'\n',
    vac_salary
)