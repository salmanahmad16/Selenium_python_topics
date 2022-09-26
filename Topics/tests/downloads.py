import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options


# Download with chrome webdriver

def chromeSetup():
    service_obj = Service("/Users/mac/PycharmProjects/Selenium_practice/Topics/driver/chromedriver")

    # Download file to desired location
    pref = {"download.default_directory": "/Users/mac/PycharmProjects/Selenium_practice/Topics/downloads"}
    option = webdriver.ChromeOptions()
    option.add_experimental_option("prefs", pref)

    driver = webdriver.Chrome(service=service_obj, options=option)

    return driver


driver = chromeSetup()

driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
driver.implicitly_wait(10)
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, 'tbody>tr:nth-of-type(1)>td:nth-child(5)>a').click()
driver.implicitly_wait(10)
