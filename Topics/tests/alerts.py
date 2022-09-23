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

driver.get("https://the-internet.herokuapp.com/javascript_alerts")



def response(message):
    response_message = driver.find_element(By.ID, 'result')
    if response_message.text == message:
        print(response_message.text)



js_alert_btn = driver.find_element(By.CSS_SELECTOR, '.example>ul>li:nth-child(1)>button')
js_alert_btn.click()

driver.implicitly_wait(4)

handle = driver.switch_to.alert

handle.accept()
driver.implicitly_wait(4)
response("You successfully clicked an alert")
time.sleep(5)


js_confirm_btn = driver.find_element(By.CSS_SELECTOR, '.example>ul>li:nth-child(2)>button')
driver.implicitly_wait(4)
js_confirm_btn.click()

handle = driver.switch_to.alert
handle.accept()
response("You clicked: Ok")
time.sleep(5)

driver.implicitly_wait(4)
js_confirm_btn.click()
driver.implicitly_wait(4)
handle = driver.switch_to.alert
handle.dismiss()
response("You clicked: Cancel")
time.sleep(5)


js_prompt_btn = driver.find_element(By.CSS_SELECTOR, '.example>ul>li:nth-child(3)>button')
js_prompt_btn.click()
driver.implicitly_wait(4)
handle = driver.switch_to.alert
handle.send_keys("salman")
driver.implicitly_wait(4)
handle.accept()
driver.implicitly_wait(4)
response("You entered: salman")
time.sleep(5)






time.sleep(3)
driver.quit()