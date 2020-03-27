from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

driver.get('https://geekbrains.ru/login')
assert "Brains - образовате" in driver.title

elem = driver.find_element_by_id('user_email')
elem.send_keys('study.ai_172@mail.ru')

elem = driver.find_element_by_id('user_password')
elem.send_keys('Password172')

elem.send_keys(Keys.RETURN)
time.sleep(1)
profile = driver.find_element_by_class_name('avatar')
driver.get(profile.get_attribute('href'))
# profile = driver.find_element_by_xpath("//a[@class='avatar']")  #@href?
# driver.get(profile.get_attribute('href'))

edit_profile = driver.find_element_by_class_name('text-sm')
driver.get(edit_profile.get_attribute('href'))

name = driver.find_element_by_name('user[first_name]')
name.send_keys(Keys.CONTROL + 'a')
name.send_keys(Keys.BACK_SPACE)




gender = driver.find_element_by_name('user[gender]')
# options = gender.find_elements_by_tag_name('option')
#
# for option in options:
#     if option.text == 'Мужской':
#         option.click()

select = Select(driver.find_element_by_name('user[gender]'))
select.select_by_value('1')

















# driver.quit()



