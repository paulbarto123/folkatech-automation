import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="class")
def setup(request):
    # Initialize WebDriver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://lapor.folkatech.com")  # Open the website
    time.sleep(3)
    # Attach the driver to the test class
    request.cls.driver = driver
    yield driver # Yield control to the test

    # Teardown after test execution
    driver.quit()