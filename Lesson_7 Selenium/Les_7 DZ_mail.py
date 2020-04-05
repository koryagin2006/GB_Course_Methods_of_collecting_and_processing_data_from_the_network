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
first_mail = driver.find_element_by_xpath("//div[@class='layout__main-frame']//a[1]")
driver.get(first_mail.get_attribute("href"))

driver.implicitly_wait(10)
mail_data = {}
mail_data['from'] = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'letter-contact'))).get_attribute('title')
mail_data['date'] = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'letter__date'))).text
mail_data['theme'] = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'thread__subject'))).text
mail_data['mail_text'] = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'letter-body__body-content'))).text
collection.insert_one(mail_data)
# pprint(mail_data)

button = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//span[@title='Следующее']")))
button.click()

# while button.clic:
#
#
# driver.quit()
