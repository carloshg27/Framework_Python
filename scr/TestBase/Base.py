import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_auto_update import check_driver
from pathlib import Path
import os


class Base:

    def __init__(self):
        self.browser = "chrome"
        self.baseurl = "https://www.google.com"
        self.driver = self.getwebdriverinstance()

    def getwebdriverinstance(self):
        if self.browser == "chrome":
            user_home = str(Path(__file__).parent.parent.parent)
            check_driver(user_home + "\\Test\\resources\\ejecutables\\")
            driverlocation = user_home + "\\Test\\resources\\ejecutables\\"
            os.environ["webdriver.chrome.driver"] = driverlocation
            chrome_options = Options()
            chrome_options.add_experimental_option("detach", True)
            self.driver = webdriver.Chrome(chrome_options)
        self.driver.implicitly_wait(30)
        return self.driver

    def navigate(self, url):
        self.driver.get(url)



base = Base()
base.navigate("https://www.google.com")
base.navigate("https://www.guru99.com/")
base.driver.maximize_window()
element = WebDriverWait(base.driver, 10).until(EC.presence_of_element_located((By.ID, "gsc-i-id1")))
element2 = base.driver.find_element(By.ID, "gsc-i-id1")
element2.send_keys("Hola Mundo")
element3 = base.driver.find_element(By.XPATH, "//button[@class='gsc-search-button gsc-search-button-v2']")
element3.click()
time.sleep(10)
