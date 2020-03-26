def photo():
    news_data = {}

    name = news_mail_photo[0].xpath("//span[@class='photo__title']/text()")[0]
    origin = ''
    href = 'https://news.mail.ru' + news_mail_photo[0].xpath("./@href")[0]
    date_time = tree(href).xpath(
        "//div[@class='article js-module js-article-swipe__content-item article-swipe-content__item "
        "m-lazy-item_complete article-swipe-content__item_active']//span[@class='article__param "
        "js-ago-wrapper']/time/@datetime")

    for i in [name, href, date_time]:
        print(i)


photo()
