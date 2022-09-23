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

driver.get("https://itera-qa.azurewebsites.net/home/automation")
driver.maximize_window()



def customRadio():

    btn = driver.find_element(By.XPATH, '//*[@id="1year"]')
    action = ActionChains(driver)
    action.click(on_element=btn)
    action.perform()

    time.sleep(3)
    driver.quit()


customRadio()

