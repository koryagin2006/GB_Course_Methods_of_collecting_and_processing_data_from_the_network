from pprint import pprint
import requests
import json

username = 'koryagin2006'
main_link = f'https://api.github.com/users/{username}/repos'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}

params = {
    'sort': 'updated'
}

response = requests.get(main_link, params=params, headers=headers)
data = json.loads(response.text)

# pprint(data)

with open("путь.json", "w", encoding="utf-8") as file:
    json.dump(data, file)
