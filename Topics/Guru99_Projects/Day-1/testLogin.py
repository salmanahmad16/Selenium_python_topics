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


# Test Case : Enter Valid user name and valid password

driver.get("https://www.demo.guru99.com/V4/index.php")      # Step-1: Go you the URL
driver.implicitly_wait(10)

user_id_input = 'input[type="text"]'
password_input = 'input[type="password"]'
login_btn = '[type="submit"]'

user_id = "mngr437961"                                                           # Test Data
password = "qYzenUj"

driver.find_element(By.CSS_SELECTOR, user_id_input).send_keys(user_id)          # Step-2: Enter Valid User Id
driver.find_element(By.CSS_SELECTOR, password_input).send_keys(password)        # Step-3: Enter Valid Password
driver.implicitly_wait(10)

driver.find_element(By.CSS_SELECTOR, login_btn).click()                         # Step-4: Click Login
driver.implicitly_wait(10)

assert "Guru99 Bank Manager HomePage" in driver.title

if driver.title == "Guru99 Bank Manager HomePage":
    print("Login Successfull")


time.sleep(2)
driver.quit()