import time
import pytest
from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from socks import PRINTABLE_PROXY_TYPES

from base.base_driver import BaseDriver

class LoginPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # Find elements and perform login
    EMAIL = "//input[@placeholder='Email']"
    PASSWORD = "//input[@id='password']"
    LOGIN_BUTTON = "//button[@type='submit']"
    RECAPTCHA_IFRAME = "//iframe[@title='reCAPTCHA']"
    CAPTCHA_CHECKING = "recaptcha-checkbox-border"
    ERROR_MESSAGE = "//label[normalize-space()='Login Gagal! Akun tidak ada.']"
    CHECK_MARK = "recaptcha-checkbox-checkmark"

    def getEmail(self):
        return self.driver.find_element(By.XPATH, self.EMAIL)

    def getPassword(self):
        return self.driver.find_element(By.XPATH, self.PASSWORD)

    def getLoginButton(self):
        return self.wait_for_element_clickable(By.XPATH, self.LOGIN_BUTTON)

    def getErrorMessage(self):
        return self.driver.find_element(By.XPATH, self.ERROR_MESSAGE)

    def getCaptchaFrame(self):
        return self.wait_for_element_available(By.XPATH, self.RECAPTCHA_IFRAME)

    def getCaptcha(self):
        return self.wait_for_element_clickable(By.CLASS_NAME, self.CAPTCHA_CHECKING)

    def getCheckMark(self):
        return self.wait_for_element_located(By.CLASS_NAME, self.CHECK_MARK)

    def enterEmail(self, email):
        self.getEmail()
        self.getEmail().send_keys(email)

    def enterPassword(self, password):
        self.getPassword()
        self.getPassword().send_keys(password)

    def captchaManual(self):
        self.getCaptchaFrame()


        self.getCaptcha()
        self.getCaptcha().click()

        # Solve the challenge manually or use AI-based automation (not recommended)
        print("🛑 Solve the CAPTCHA manually and press Enter to continue...")
        time.sleep(10)
        self.getCheckMark()

        # Switch back to main content
        self.driver.switch_to.default_content()




    def clickCaptcha(self):
        self.getCaptchaFrame()
        self.getCaptcha()
        self.getCaptcha().click()
        time.sleep(5)
        self.getCheckMark()

        # Switch back to the main content
        self.driver.switch_to.default_content()

    def clickLogin(self):
        self.getLoginButton().click()