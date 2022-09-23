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
serviceObj = Service("/Topics/driver/chromedriver")
driver = webdriver.Chrome(service=serviceObj, options=options)

driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")

driver.implicitly_wait(5)

result = driver.find_element(By.CSS_SELECTOR, '.example>p')

if result.text == "Congratulations! You must have the proper credentials.":
    print("Auth Successful")

