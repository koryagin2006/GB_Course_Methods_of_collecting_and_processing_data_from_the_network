import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # Keys - объект, содержащий все клавиши клавиатуры
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome("C:\\Users\\carne\\Desktop\\Geek "
                          "Brains\\GitHub\\GB_Course_Methods_of_collecting_and_processing_data_from_the_network"
                          "\\Lesson_7 Selenium\\chromedriver")

driver.get('https://account.mail.ru/login')
assert 'Авторизация' in driver.title

# Ввод логина
driver.implicitly_wait(10)
my_dynamic_element = driver.find_element_by_xpath("//input[@placeholder='Имя аккаунта']")
my_dynamic_element.send_keys('study.ai_172@mail.ru')
my_dynamic_element.send_keys(Keys.RETURN)

# Ввод пароля
driver.implicitly_wait(10)
my_dynamic_element = driver.find_element_by_xpath("//input[@placeholder='Пароль']")
my_dynamic_element.send_keys('NewPassword172')
my_dynamic_element.send_keys(Keys.RETURN)

# Листание
while True:
    try:
        button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'list-letter-spinner llct '
                                                           'list-letter-spinner_defaultlist-letter-spinner_hidden'))
        )
        button.send_keys()
        pages += 1
        print(f'раскрыта {pages} страница')
    except Exception as e:
        break
        print('Парсинг окончен или ошибка: ', e)

mail_list = driver.find_element_by_class_name('llc js-tooltip-direction_letter-bottom js-letter-list-item llc_normal')

# driver.quit()
