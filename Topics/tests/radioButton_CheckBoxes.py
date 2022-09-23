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

driver.get("https://itera-qa.azurewebsites.net/home/automation")


def selectGender(gender):
    all_gender = driver.find_elements(By.CSS_SELECTOR, '.card-body .form-check>label>input[name="optionsRadios"]')

    for genders in all_gender:
        value = genders.get_attribute('id')
        if value == gender:
            driver.find_element(By.ID, value).click()

    time.sleep(3)
    driver.quit()


# selectGender("female")

def selectCheckBoxes(day):
    all_checkboxes = driver.find_elements(By.CSS_SELECTOR, '.card-body .form-check>label>input[type="checkbox"]')
    driver.implicitly_wait(5)
    for checkbox in all_checkboxes:
        value = checkbox.get_attribute('id')
        for d in day:
            if value == d:
                checkbox.click()

    time.sleep(3)
    driver.quit()


days = ["monday", "tuesday", "sunday"]

selectCheckBoxes(days)
