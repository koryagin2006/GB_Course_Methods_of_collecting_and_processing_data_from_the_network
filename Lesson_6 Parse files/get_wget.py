###Загружаем с помощью requests
import requests
file = requests.get('https://klike.net/uploads/posts/2019-07/1562069947_1.jpg','sea.jpg')
with open('sea.jpg','wb') as f:
    f.write(file.content)


###Загружаем с помощью wget
import wget
wget.download('https://klike.net/uploads/posts/2019-07/1562069947_1.jpg','sea.jpg')








