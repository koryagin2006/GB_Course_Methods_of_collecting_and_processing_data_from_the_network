import time
from selenium import webdriver  # импорт webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # Keys - объект, содержащий все клавиши клавиатуры
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome \
    ("C:\\Users\\carne\\Desktop\\Geek Brains\\GitHub\\GB_Course_Methods_of_collecting_and_processing_data_from_the_network\\Lesson_7 Selenium\\chromedriver")

driver.get('https://account.mail.ru/login')
assert 'Авторизация' in driver.title

# Ввод логина
try:
    elem = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located ((By.XPATH, "//input[@placeholder='Имя аккаунта']"))
    )
    elem.send_keys('study.ai_172@mail.ru')
    elem.send_keys(Keys.RETURN)
except Exception as e:
    print('Ошибка ввода логина',e)

# Ввод пароля
try:
    elem = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located ((By.XPATH, "//input[@placeholder='Пароль']"))
    )
    elem.send_keys('NewPassword172')
    elem.send_keys(Keys.RETURN)
except Exception as e:
    print('Ошибка ввода пароля',e)



# окончание листания = //a[@class='list-letter-spinner llct list-letter-spinner_default list-letter-spinner_hidden']

# list = //a[@class='llc js-tooltip-direction_letter-bottom js-letter-list-item llc_normal']

# driver.quit()