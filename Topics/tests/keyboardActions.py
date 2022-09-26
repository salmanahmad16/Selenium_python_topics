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

driver.get("https://demoqa.com/text-box")

driver.implicitly_wait(10)

name = driver.find_element(By.ID, 'userName')
name.send_keys("Welcome")
driver.implicitly_wait(10)

act = ActionChains(driver)

act.key_down(Keys.COMMAND).send_keys("a").key_up(Keys.COMMAND).perform()        # Select text
time.sleep(4)
act.key_down(Keys.COMMAND).send_keys("c").key_up(Keys.COMMAND).perform()        # Copy text
time.sleep(4)
act.send_keys(Keys.TAB).perform()                                   # Tab to next text area
time.sleep(4)

act.key_down(Keys.COMMAND).send_keys("v").key_up(Keys.COMMAND).perform()        # Paste into next text area



time.sleep(4)
driver.quit()