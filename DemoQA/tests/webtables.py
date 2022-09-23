import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains

serviceObj = Service("/Users/mac/PycharmProjects/Selenium_practice/DemoQA/driver/chromedriver")
driver = webdriver.Chrome(service=serviceObj)

driver.get("https://testautomationpractice.blogspot.com/")

# count numbers of row and columns of webtables
rows = len(driver.find_elements(By.CSS_SELECTOR, '.widget-content>table>tbody>tr'))
columns = len(driver.find_elements(By.CSS_SELECTOR, '.widget-content>table>tbody>tr>th'))

print("Rows are > ", rows)
print("Columns are > ", columns)

# Get the book name which price is 300
driver.implicitly_wait(10)
for i in range(2, rows + 1):
    driver.implicitly_wait(2)
    price = driver.find_element(By.XPATH, f'//div[@class="widget-content"]/table/tbody/tr[{i}]/td[4]').text
    if price == "300":
        bookname = driver.find_element(By.XPATH, f'//div[@class="widget-content"]/table/tbody/tr[{i}]/td[1]').text
        print(bookname)

time.sleep(4)
driver.quit()
