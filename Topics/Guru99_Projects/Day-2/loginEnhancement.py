import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from utilities_login import utilities

options = Options()
options.headless = False
serviceObj = Service("/Users/mac/PycharmProjects/Selenium_practice/Topics/driver/chromedriver")
driver = webdriver.Chrome(service=serviceObj, options=options)


user_id_input = 'input[type="text"]'
password_input = 'input[type="password"]'
login_btn = '[type="submit"]'


util = utilities(driver)

util.setup()                # step-1: go to the page

driver.find_element(By.CSS_SELECTOR, user_id_input).send_keys(util.user_id)
driver.find_element(By.CSS_SELECTOR, password_input).send_keys(util.password)
driver.implicitly_wait(10)

driver.find_element(By.CSS_SELECTOR, login_btn).click()                         # Step-4: Click Login
driver.implicitly_wait(10)

assert util.manager_page_title in driver.title

if util.manager_page_title == driver.title:
    print("Login Successfully")


time.sleep(2)
driver.quit()




