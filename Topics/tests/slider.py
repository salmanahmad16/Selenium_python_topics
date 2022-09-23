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

driver.implicitly_wait(10)
driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.implicitly_wait(10)

min_value = driver.find_element(By.CSS_SELECTOR, '#slider-range>:nth-child(2)')
max_value = driver.find_element(By.CSS_SELECTOR, '#slider-range>:nth-child(3)')

print("Location before move ... > ", min_value.location)  # {'x': 59, 'y': 251}
print("Location before move ... > ", max_value.location)  # {'x': 485, 'y': 251}


act = ActionChains(driver)

act.drag_and_drop_by_offset(min_value, 100, 0).perform()
print("Location After move ... > ", min_value.location)

act.drag_and_drop_by_offset(max_value, -100, 0).perform()
print("Location After move ... > ", max_value.location)

time.sleep(4)
driver.quit()
