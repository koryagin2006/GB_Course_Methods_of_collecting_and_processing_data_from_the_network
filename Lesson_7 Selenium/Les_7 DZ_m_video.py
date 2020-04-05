from pymongo import MongoClient
from selenium import webdriver  # импорт webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""
2) Написать программу, которая собирает «Хиты продаж» с сайта техники mvideo и складывает данные в БД. 
Магазины можно выбрать свои. Главный критерий выбора: динамически загружаемые товары
"""

client = MongoClient('localhost', 27017)
db = client['Lesson_7']
collection = db.m_video

chrome_options = Options()
chrome_options.add_argument('start-maximized')
chrome_options.add_argument('--headless')  # включить, когда окно браузера не нужно
driver = webdriver.Chrome("C:\\Users\\carne\\Desktop\\Geek "
                          "Brains\\GitHub\\GB_Course_Methods_of_collecting_and_processing_data_from_the_network"
                          "\\Lesson_7 Selenium\\chromedriver", options=chrome_options)
driver.get('https://www.mvideo.ru/')
assert 'М.Видео - ' in driver.title

while True:
    elem = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//div[@class="gallery-content accessories-new "][1]//a[contains(@class,"sel-hits-button-next")]')))
    if 'disabled' in elem.get_attribute('class'):
        break
    else:
        elem.click()

elem_2 = driver.find_element_by_xpath("//div[@class='gallery-content accessories-new ']")
# elem_2 = driver.find_element_by_class_name('gallery-content accessories-new ')
product_list = elem_2.find_elements_by_class_name('gallery-list-item')

for product in product_list:
    product_data = {}
    product_data['name'] = product.find_element_by_class_name('sel-product-tile-title').get_attribute('title')
    product_data['link'] = product.find_element_by_class_name('sel-product-tile-title').get_attribute('href')
    product_data['price'] = product.find_element_by_class_name('c-pdp-price__current').text
    collection.insert_one(product_data)
print('Finish!')
driver.quit()
