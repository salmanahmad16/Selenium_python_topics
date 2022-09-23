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

driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")

driver.switch_to.frame('packageListFrame')
first_frame = driver.find_element(By.LINK_TEXT, 'org.openqa.selenium')
first_frame.click()

driver.switch_to.default_content()

driver.switch_to.frame('packageFrame')
second_frame = driver.find_element(By.LINK_TEXT, 'OutputType')
second_frame.click()

driver.switch_to.default_content()

driver.implicitly_wait(5)
driver.switch_to.frame('classFrame')
third_frame = driver.find_element(By.CSS_SELECTOR, '.topNav>ul>li:nth-child(5)')
third_frame.click()

time.sleep(3)
driver.quit()

