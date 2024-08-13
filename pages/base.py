"""
This module contains the BasePage class which provides common
functionalities for interacting with web pages using Selenium WebDriver.
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """
    A base page class that encapsulates common functionalities
    for interacting with web pages using Selenium WebDriver.
    """
    def __init__(self, driver):
        """
        Initializes the BasePage with the provided WebDriver
        instance and sets up the WebDriverWait.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator):
        """
        Finds an element on the page using the provided locator.
        """
        return self.wait.until(EC.presence_of_element_located(locator))

    def click_element(self, locator):
        """
        Clicks on an element located by the provided locator.
        """
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def enter_text(self, locator, text):
        """
        Enters text into an input field located by the provided locator.

        Returns:
            bool:
                True if the text was successfully entered, False otherwise.
        """
        element = self.find_element(locator)
        if element:
            element.clear()
            element.send_keys(text)
            return True
        return False
