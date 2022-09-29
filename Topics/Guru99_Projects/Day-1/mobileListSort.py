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

driver.get("http://live.techpanda.org/index.php/")  # Step-1 Go to URL
driver.maximize_window()
driver.implicitly_wait(10)
getPageTitleText = '//div[@class="page-title"]/h2'

pageTitle = driver.find_element(By.XPATH, getPageTitleText)  # Get page title
driver.implicitly_wait(10)
assert "THIS IS DEMO SITE FOR" in pageTitle.text  # Step-2 Verify Page title text

mobile_menu_btn = driver.find_element(By.LINK_TEXT, 'MOBILE')
mobile_menu_btn.click()  # Step-3 Click on Mobile menu
time.sleep(3)
driver.implicitly_wait(10)
assert 'Mobile' in driver.title  # Step-4 Verify Title

get_dropDown_list = driver.find_element(By.CSS_SELECTOR,
                                        'div.col-wrapper > div.col-main > div.category-products > div.toolbar > div.sorter > div > select')
time.sleep(3)
select = Select(get_dropDown_list)

select.select_by_visible_text("Name")  # Step-5 Sorted as name
time.sleep(3)

get_dropDown = driver.find_element(By.CSS_SELECTOR,
                                   'div.col-wrapper > div.col-main > div.category-products > div.toolbar > div.sorter > div > select')

if get_dropDown.is_selected():
    print("Verified")  # Validate name is selected in dropdown
