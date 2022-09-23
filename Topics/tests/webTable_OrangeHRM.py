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
serviceObj = Service("/Users/mac/PycharmProjects/Selenium_practice/Topics/driver/chromedriver")
driver = webdriver.Chrome(service=serviceObj, options=options)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.implicitly_wait(20)
driver.find_element(By.CSS_SELECTOR, 'input[name="username"]').send_keys("Admin")
driver.implicitly_wait(10)
driver.find_element(By.CSS_SELECTOR, 'input[name="password"]').send_keys("admin123")
driver.implicitly_wait(10)
driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
driver.implicitly_wait(10)
driver.find_element(By.CSS_SELECTOR, '.oxd-main-menu>li:nth-child(1)>a').click()
driver.implicitly_wait(10)

elements = driver.find_elements(By.CSS_SELECTOR, '.oxd-table>div:nth-child(2)>div>div>div:nth-child(5)')
driver.implicitly_wait(10)

names = driver.find_elements(By.CSS_SELECTOR, '.oxd-table>div:nth-child(2)>div>div>div:nth-child(2)')


count = 0
for elm in elements:
    if elm.text == "Enabled":
        count = count+1

print("Total enabled > ", count)

time.sleep(4)
driver.quit()