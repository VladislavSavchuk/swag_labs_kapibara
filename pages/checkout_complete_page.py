"""
This module contains the CheckoutCompletePage class, which provides
functionalities specific to the 'Checkout: Complete!' page of the application.
"""

from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from pages.base import BasePage


class CheckoutCompletePage(BasePage):
    """
    Class representing the 'Checkout: Complete!' page of the application.
    """

    def __init__(self, driver):
        """
        Initializes CheckoutCompletePage and sets up locators and methods for
        'Checkout: Complete!' page.
        """
        super().__init__(driver)
        self.page_title = (By.CLASS_NAME, "title")

        self.complete_icon = (By.CLASS_NAME, "pony_express")
        self.complete_header = (By.CLASS_NAME, "complete-header")
        self.complete_description = (By.CLASS_NAME, "complete-text")
        self.back_home_button = (By.NAME, "back-to-products")

    def get_page_title(self):
        """ Returns page title text """
        return self.get_text(self.page_title)

    def check_page_elements(self):
        """ Finds inputs for user info, returns False otherwise """
        try:
            self.find_element(self.complete_icon)
            self.find_element(self.complete_header)
            self.find_element(self.complete_description)
            self.find_element(self.back_home_button)

        except TimeoutException:
            return False
        return True

    def get_complete_header_text(self):
        """ Returns text of the header """
        return self.get_text(self.complete_header)

    def get_complete_description_text(self):
        """ Returns text of the description """
        return self.get_text(self.complete_description)

    def click_back_home_button(self):
        """ Clicks 'Back Home' button """
        self.click_element(self.back_home_button)
