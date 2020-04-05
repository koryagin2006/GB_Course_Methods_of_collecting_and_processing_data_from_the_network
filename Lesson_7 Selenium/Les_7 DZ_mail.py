import time
from pprint import pprint

from pymongo import MongoClient
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # Keys - объект, содержащий все клавиши клавиатуры
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
from lxml import html

"""
1) Написать программу, которая собирает входящие письма из своего или тестового почтового ящика и
сложить данные о письмах в базу данных (
- от кого,
- дата отправки,
- тема письма,
- текст письма полный)
Логин тестового ящика: study.ai_172@mail.ru
Пароль тестового ящика: NewPassword172
"""
login = 'study.ai_172@mail.ru'
password = 'NewPassword172'

client = MongoClient('localhost', 27017)
db = client['Lesson_7']
collection = db.mailru

chrome_options = Options()
chrome_options.add_argument('start-maximized')
# chrome_options.add_argument('--headless')  # включить, когда окно браузера не нужно
driver = webdriver.Chrome("C:\\Users\\carne\\Desktop\\Geek "
                          "Brains\\GitHub\\GB_Course_Methods_of_collecting_and_processing_data_from_the_network"
                          "\\Lesson_7 Selenium\\chromedriver", options=chrome_options)
driver.get('https://account.mail.ru/login')
assert 'Авторизация' in driver.title

# Ввод логина
driver.implicitly_wait(10)
elem = driver.find_element_by_xpath("//input[@placeholder='Имя аккаунта']")
elem.send_keys(login)
elem.send_keys(Keys.RETURN)

# Ввод пароля
driver.implicitly_wait(10)
elem = driver.find_element_by_xpath("//input[@placeholder='Пароль']")
elem.send_keys(password)
elem.send_keys(Keys.RETURN)

# Первое письмо
first_mail = driver.find_element_by_xpath("//div[@class='layout__main-frame']//a[1]").get_attribute('href')
driver.get(first_mail)

driver.implicitly_wait(10)
mail_data = {}
mail_data['from'] = driver.find_element_by_class_name('letter-contact').get_attribute('title')
mail_data['date'] = driver.find_element_by_class_name('letter__date').text
mail_data['theme'] = driver.find_element_by_class_name('thread__subject').text
mail_data['mail_text'] = driver.find_element_by_class_name('letter-body__body-content').text
collection.insert_one(mail_data)
# pprint(mail_data)
for i in range(10000):
    print(f'Собрано писем: {i+1}')
    # time.sleep(2)
    driver.implicitly_wait(10)
    webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys(Keys.ARROW_DOWN).perform()
    mail_data = {}
    mail_data['from'] = driver.find_element_by_class_name('letter-contact').get_attribute('title')
    try:
        mail_data['date'] = driver.find_element_by_class_name('letter__date').text
    except Exception as e:
        mail_data['date'] = None
    try:
        mail_data['mail_text'] = driver.find_element_by_class_name('letter-body__body-content').text
    except Exception as e:
        mail_data['mail_text'] = None
    collection.insert_one(mail_data)
    if driver.find_element_by_xpath(
            "//div[@class='portal-menu-element portal-menu-element_next portal-menu-element_expanded portal-menu-element_not-touch']/span"
    ).get_attribute(
        'class') == 'button2 button2_has-ico button2_arrow-down button2_pure button2_short button2_ico-text-top button2_hover-support button2_disabled js-shortcut':
        break

# driver.quit()
