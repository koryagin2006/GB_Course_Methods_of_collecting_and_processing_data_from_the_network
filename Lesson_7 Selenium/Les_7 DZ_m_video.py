import time
from selenium import webdriver  # импорт webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # Keys - объект, содержащий все клавиши клавиатуры
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome \
    (
        "C:\\Users\\carne\\Desktop\\Geek Brains\\GitHub\\GB_Course_Methods_of_collecting_and_processing_data_from_the_network\\Lesson_7 Selenium\\chromedriver")

driver.get('https://www.mvideo.ru/')
assert 'М.Видео - ' in driver.title


time.sleep(5)

elem = driver.find_elements_by_xpath("//a[@class='next-btn sel-hits-button-next']")
elem[1].click()


# driver.quit()
