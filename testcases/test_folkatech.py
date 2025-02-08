import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from config.configtest import setup
import time

from base.base_driver import BaseDriver
from utilities.utils import Utils
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup")
class TestFolkatech():


    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.login_page = LoginPage(self.driver)
        self.USERNAME = "rhmtsaepuloh@gmail.com"  # Replace with a valid username
        self.PASSWORD = "password"  # Replace with a valid password

    # Positive Test Case - Valid Login
    def test_valid_login(self):
        time.sleep(2)  # Wait for page load

        # Find elements and perform login
        self.login_page.enterEmail(self.USERNAME)
        self.login_page.enterPassword(self.PASSWORD)
        self.login_page.captchaManual()
        self.login_page.clickLogin()
        time.sleep(3)
        # Validate successful login
        try:
            assert "dashboard" in self.driver.current_url.lower(), "Login failed!"
            print("✅ Positive Test: Login successful!")
        except AssertionError as e:
            Utils.take_screenshot("valid_login_fail")
            print(f"❌ Positive Test Failed: {e}")

    # Negative Test Case - Invalid Login
    def test_invalid_login(self):
        time.sleep(2)
        # Find elements and perform login with wrong credentials
        self.login_page.enterEmail(self.USERNAME)
        self.login_page.enterPassword(self.PASSWORD)
        self.login_page.clickLogin()
        time.sleep(3)

        # Validate error message
        try:
            error_msg = self.login_page.getErrorMessage().text
            assert "invalid credentials" in error_msg.lower(), "Expected error message not found!"
            print("✅ Negative Test: Error message displayed correctly!")
        except AssertionError as e:
            Utils.take_screenshot("invalid_login_fail")
            print(f"❌ Negative Test Failed: {e}")