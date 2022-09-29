from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class utilities:
    h2_text = '//h2[@class="barone"]'
    base_url = 'https://www.demo.guru99.com/V4/index.php'
    user_id = "mngr437961"
    password = "qYzenUj"
    manager_page_title = 'Guru99 Bank Manager HomePage'

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def setup(self):
        self.driver.get(self.base_url)

    def get_text(self):
        return self.wait.until(EC.presence_of_element_located((By.XPATH, self.h2_text))).text
