"""
This module contains the LoginPage class, which provides functionalities
specific to the login page of the application.
"""

import logging
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from pages.base import BasePage
from test_data import login_creds


class LoginPage(BasePage):
    """
    Class representing the login page of the application.
    Inherits from BasePage to provide common page functionalities.
    """

    def __init__(self, driver):
        """
        Initializes the LoginPage with the provided WebDriver instance
        and sets up the locators for the login page elements.
        """
        super().__init__(driver)
        self.input_username = (By.ID, "user-name")
        self.input_password = (By.ID, "password")
        self.login_btn = (By.ID, "login-button")
        self.error_msg = (By.TAG_NAME, "h3")

    def login(self, username=login_creds.STANDARD_USER,
              password=login_creds.STANDARD_PASSWORD):
        """
        Completes the login process by entering the provided username
        and password, and submitting the login form.
        """
        self.enter_text(self.input_username, username)
        self.enter_text(self.input_password, password)

        self.click_element(self.login_btn)

    def error_message_exists(self):
        """
        Checks if an error message is displayed on the login page.

        Returns:
            bool: True if an error message exists, False otherwise.
        """
        try:
            error_message = self.driver.find_elements(*self.error_msg)
            logging.info(f"Error message: {bool(error_message)}")
            return bool(error_message)
        except TimeoutException:
            logging.info("Error message did not appear.")
            return False
