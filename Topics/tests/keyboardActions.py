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

driver.get("https://text-compare.com/")

driver.implicitly_wait(10)

text_area_1 = driver.find_element(By.CSS_SELECTOR, '[name="text1"]')
text_area_1.send_keys("Welcome")
driver.implicitly_wait(10)
text_area_2 = driver.find_element(By.CSS_SELECTOR, '[name="text2"]')

act = ActionChains(driver)
driver.implicitly_wait(10)
act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()        # Select text

act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()        # Copy text

act.send_keys(Keys.TAB).perform()                                   # Tab to next text area
driver.implicitly_wait(10)
act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()        # Paste into next text area

