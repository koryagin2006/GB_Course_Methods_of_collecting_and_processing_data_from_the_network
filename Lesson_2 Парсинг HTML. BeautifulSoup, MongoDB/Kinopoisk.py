from bs4 import BeautifulSoup as bs
import requests
from pprint import pprint
main_link = 'https://www.kinopoisk.ru'
html = requests.get(main_link + '/afisha/new/city/1/').text
parsed_html = bs(html,'lxml')

films_block = parsed_html.find('div',{'class':'filmsListNew js-rum-hero'})
films_list = films_block.findChildren(recursive=False)

films = []
for film in films_list:
    film_data={}
    main_info = film.find('div',{'class':'name'}).findChild()
    film_name = main_info.getText().replace('xa0','')
    film_link = main_link + main_info['href']
    genre = film.find_all('div',{'class':'gray'})[1].getText().replace(' ','')[9:]
    rating = film.find('span',{'class':['rating_ball_grey','rating_ball_green','rating_ball_red']})
    if not rating:
        rating = 0
    else:
        rating = rating.getText()

    film_data['name'] = film_name
    film_data['link'] = film_link
    film_data['genre'] = genre
    film_data['rating'] = rating

    films.append(film_data)

pprint(films)






