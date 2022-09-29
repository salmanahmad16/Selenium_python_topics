import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

options = Options()
options.headless = False
serviceObj = Service("/Users/mac/PycharmProjects/Selenium_practice/Topics/driver/chromedriver")
driver = webdriver.Chrome(service=serviceObj, options=options)

driver.get("http://live.techpanda.org/")        # Step-1: Go to URL
driver.implicitly_wait(10)
driver.find_element(By.LINK_TEXT, 'MOBILE').click()    # Step-2: Click on Mobile


list_page_price = driver.find_element(By.CSS_SELECTOR, '.price-box>span[id="product-price-1"]').text  # Step-3: Value noted of mobile

mobile = driver.find_element(By.CSS_SELECTOR, '.product-name>a[title="Sony Xperia"]')

mobile.click()                                                          # Click on Sony Xperia
driver.implicitly_wait(10)

detail_page_price = driver.find_element(By.CSS_SELECTOR, '#product-price-1>span').text      # Get price from detail page
driver.implicitly_wait(10)

if list_page_price == detail_page_price:
    print("Price Verified")






