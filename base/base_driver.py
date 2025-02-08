import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BaseDriver:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element_clickable(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 5)
        element = wait.until(EC.element_to_be_clickable((locator_type, locator)))
        return element