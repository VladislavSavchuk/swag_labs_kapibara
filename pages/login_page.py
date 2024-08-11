"""
This module contains the LoginPage class, which provides functionalities
specific to the login page of the application.
"""

import logging
from selenium.common import TimeoutException
from pages.locators.login_page_locators import LoginPageLocators
from pages.base import BasePage


class LoginPage(BasePage):
    """
    Class representing the login page of the application.
    Inherits from BasePage to provide common page functionalities.
    """

    def __init__(self, driver):
        """
        Initializes the LoginPage with the provided WebDriver instance
        and sets up the locators for the login page elements.

        Parameters:
            driver (selenium.webdriver.remote.webdriver.WebDriver):
                The WebDriver instance used to interact with the browser.
        """
        super().__init__(driver)
        self.input_username = LoginPageLocators.input_username
        self.input_password = LoginPageLocators.input_password
        self.login_btn = LoginPageLocators.login_btn
        self.error_msg = LoginPageLocators.error_msg

    def login(self, username, password):
        """
        Completes the login process by entering the provided username
        and password, and submitting the login form.

        Parameters:
            username (str): The username to be entered in the login form.
            password (str): The password to be entered in the login form.
        """
        self.enter_text(LoginPageLocators.input_username, username)
        self.enter_text(LoginPageLocators.input_password, password)

        self.click_element(LoginPageLocators.login_btn)

    def error_message_exists(self):
        """
        Checks if an error message is displayed on the login page.

        Returns:
            bool: True if an error message exists, False otherwise.

        Logs:
            Logs the presence or absence of an error message on the page.

        Raises:
            TimeoutException: If the error message is not found within
            the expected time.
        """
        try:
            error_message = self.driver.find_elements(*self.error_msg)
            logging.info(f"Error message: {bool(error_message)}")
            return bool(error_message)
        except TimeoutException:
            logging.info("Error message did not appear.")
            return False
