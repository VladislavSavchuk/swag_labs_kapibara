"""This module contains the fixtures for the tests"""

import pytest
from selenium import webdriver
from test_data.ui.constants import URL


@pytest.fixture()
def driver():
    """
    Fixture that provides a WebDriver instance for the tests.

    This fixture initializes the Chrome WebDriver with specified options,
    sets an implicit wait time, and navigates to the predefined URL.
    It ensures that the browser is opened before the test and properly
    closed after the test.
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(2)
    browser.get(URL)
    yield browser
    browser.quit()
