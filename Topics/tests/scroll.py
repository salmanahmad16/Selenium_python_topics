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

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.implicitly_wait(10)


                            #scroll by pixel

def scrollByPixel():
    driver.execute_script("window.scrollBy(0, 3000)", "")
    pixel = driver.execute_script("return window.pageYOffset;")

    print("number of pixel : ", pixel)

#scrollByPixel()



                        #scroll by index, value, text

def scrollByValue():
    flag = driver.find_element(By.XPATH, '//img[@alt="Flag of Pakistan"]')
    driver.execute_script("arguments[0].scrollIntoView();", flag)

#scrollByValue()

                        #scroll down page to end
def scrollDownToEnd():
    driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")

scrollDownToEnd()


                        #scroll up to top
def scrollUpToTop():
    driver.execute_script("window.scrollBy(0, -document.body.scrollHeight)")


scrollDownToEnd()
time.sleep(1)
scrollUpToTop()

time.sleep(3)
driver.quit()