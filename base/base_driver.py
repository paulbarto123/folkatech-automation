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

    def wait_for_element_available(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.frame_to_be_available_and_switch_to_it((locator_type, locator)))
        return element

    def wait_for_element_located(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 5)
        element = wait.until(EC.presence_of_element_located((locator_type, locator)))
        return element