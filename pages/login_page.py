import time
import pytest
from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys

from base.base_driver import BaseDriver

class LoginPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # Find elements and perform login
    EMAIL = "email"
    PSSWORD = "password"
    LOGIN_BUTTON = "//button[text()='Login']"
    ERROR_MESSAGE = "error-message"

    def getEmail(self):
        return self.driver.find_element(By.NAME, self.EMAIL)

    def getPassword(self):
        return self.driver.find_element(By.NAME, self.PSSWORD)

    def getLoginButton(self):
        return self.wait_for_element_clickable(By.XPATH, self.LOGIN_BUTTON)

    def getErrorMessage(self):
        return self.driver.find_element(By.CLASS_NAME, self.ERROR_MESSAGE)

    def enterEmail(self, email):
        self.getEmail()
        self.getEmail().send_keys(email)

    def enterPassword(self, password):
        self.getPassword()
        self.getPassword().send_keys(password)

    def clickLogin(self):
        self.getLoginButton().click()