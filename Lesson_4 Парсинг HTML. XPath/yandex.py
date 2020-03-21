from pprint import pprint
from lxml import html
import requests

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
def request_to_yandex(str):
    try:
        response = requests.get('https://yandex.ru/search/',
                                params={'text':str},
                                headers = header
                                )
        tree = html.fromstring(response.text)
        result = tree.xpath("//a[contains(@class,'organic__url_type_multiline')]/@href | //a[contains(@class,'link_cropped_no')]/@href")
        return result
    except Exception as e:
        print(e)


result = request_to_yandex('суши')

pprint(result)
