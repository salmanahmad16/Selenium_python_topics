import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = False
serviceObj = Service("/Users/mac/PycharmProjects/Selenium_practice/DemoQA/driver/chromedriver")
driver = webdriver.Chrome(service=serviceObj, options=options)

driver.get("https://jqueryui.com/datepicker/")

# Datepicker with simple send keys
driver.implicitly_wait(10)
driver.switch_to.frame(0)
driver.implicitly_wait(10)
# driver.find_element(By.CSS_SELECTOR, 'input#datepicker').send_keys("09/21/2022")


# Datepicker with clicks
driver.find_element(By.CSS_SELECTOR, 'input#datepicker').click()
driver.implicitly_wait(10)
driver.find_element(By.CSS_SELECTOR, '[title="Prev"]').click()  # click on previous month
driver.find_element(By.CSS_SELECTOR, '[data-date="16"]').click()
driver.implicitly_wait(10)

# Date picker with logic and loop

es_year = "2000"
es_month = "August"
es_day = "16"

driver.find_element(By.CSS_SELECTOR, 'input#datepicker').click()
while True:
    driver.implicitly_wait(10)
    driver.find_element(By.CSS_SELECTOR, '[title="Prev"]').click()
    month = driver.find_element(By.CSS_SELECTOR, '.ui-datepicker-month').text
    year = driver.find_element(By.CSS_SELECTOR, '.ui-datepicker-year').text
    if month == es_month and year == es_year:
        driver.implicitly_wait(10)
        driver.find_element(By.CSS_SELECTOR, '[data-date="16"]').click()
        driver.implicitly_wait(10)
        break

print(month, year)







time.sleep(5)
driver.quit()
