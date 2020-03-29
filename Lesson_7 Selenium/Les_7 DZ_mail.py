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

# Листание


mail_list = driver.find_element_by_class_name('llc js-tooltip-direction_letter-bottom js-letter-list-item llc_normal')
# driver.quit()