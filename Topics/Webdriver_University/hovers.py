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

driver.get("https://webdriveruniversity.com/Scrolling/index.html")
driver.implicitly_wait(5)
scroll = driver.find_element(By.CSS_SELECTOR, '[id="zone1"]')

act = ActionChains(driver)
driver.implicitly_wait(5)
act.move_to_element(scroll)
time.sleep(3)
act.perform()
driver.implicitly_wait(5)

entry1 = driver.find_element(By.CSS_SELECTOR, '[id="zone2"]')
entry2 = driver.find_element(By.CSS_SELECTOR, '[id="zone3"]')

for i in range(10):
    act.move_to_element(entry1)
    time.sleep(0.1)
    act.perform()
    act.move_to_element(entry2)
    time.sleep(0.1)
    act.perform()

time.sleep(3)
driver.quit()
