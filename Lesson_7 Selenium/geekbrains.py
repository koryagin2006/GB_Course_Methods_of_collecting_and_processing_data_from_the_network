import time
from selenium import webdriver  # импорт webdriver
from selenium.webdriver.common.keys import Keys  # Keys - объект, содержащий все клавиши клавиатуры

driver = webdriver.Chrome \
    ("C:\\Users\\carne\\Desktop\\Geek Brains\\GitHub\\GB_Course_Methods_of_collecting_and_processing_data_from_the_network\\Lesson_7 Selenium\\chromedriver")
driver.get('https://geekbrains.ru/login')
assert 'Вход | GeekBrains' in driver.title

# time.sleep(5)
elem = driver.find_element_by_id('user_email')
elem.send_keys('study.ai_172@mail.ru')

elem = driver.find_element_by_id('user_password')
elem.send_keys('Password172')

elem.send_keys(Keys.RETURN)

profile = driver.find_element_by_class_name('avatar')
driver.get(profile.get_attribute('href'))

edit_profile = driver.find_element_by_class_name('text-sm')
driver.get(edit_profile.get_attribute('href'))

