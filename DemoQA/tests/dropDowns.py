import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select

options = Options()
options.headless = False
serviceObj = Service("/Users/mac/PycharmProjects/Selenium_practice/DemoQA/driver/chromedriver")
driver = webdriver.Chrome(service=serviceObj, options=options)

driver.get("https://itera-qa.azurewebsites.net/home/automation")

dropdown = driver.find_element(By.CLASS_NAME, 'custom-select')

dropSelect = Select(dropdown).select_by_index(2)

