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

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

driver.implicitly_wait(10)
driver.find_element(By.LINK_TEXT, 'OrangeHRM, Inc').click()
driver.implicitly_wait(10)

windowsId = driver.window_handles

parentWindow = windowsId[0]
childWindow = windowsId[1]

driver.switch_to.window(childWindow)

title = driver.title

if title == 'OrangeHRM HR Software | Free & Open Source HR Software | HRMS | HRIS | OrangeHRM':
    print("OK")

