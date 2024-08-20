"""
This module contains the CheckoutInfoPage class, which provides
functionalities specific to the 'Checkout: Your information' page of the
application.
"""

from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from pages.base import BasePage
from test_data import checkout_info


class CheckoutInfoPage(BasePage):
    """
    Class representing the 'Checkout: Your information' page of the
    application.
    """

    def __init__(self, driver):
        """
        Initializes CheckoutInfoPage and sets up locators and methods for
        'Checkout: Your information' page.
        """
        super().__init__(driver)
        self.page_title = (By.CLASS_NAME, "title")

        self.checkout_info_form = (By.CLASS_NAME, "checkout_info")
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")

        self.error_icons = (By.CSS_SELECTOR, "[data-icon='times-circle']")
        self.error_message_container = (
            By.CLASS_NAME, "error-message-container")
        self.error_text = (By.CSS_SELECTOR, "[data-test='error']")
        self.cancel_button = (By.ID, "cancel")
        self.continue_button = (By.ID, "continue")

    def get_page_title(self):
        """ Returns page title text """
        return self.get_text(self.page_title)

    def check_page_elements(self):
        """ Finds inputs for user info, returns False otherwise """
        elements = [self.first_name_input,
                    self.last_name_input,
                    self.postal_code_input,
                    self.cancel_button,
                    self.continue_button]
        try:
            for element in elements:
                self.find_element(element)

        except TimeoutException:
            return False
        return True

    def enter_checkout_first_name(self,
                                  first_name=checkout_info.FIRST_NAME_VALID):
        """ Fills first name input with provided info """
        self.enter_text(self.first_name_input, first_name)

    def enter_checkout_last_name(self,
                                 last_name=checkout_info.LAST_NAME_VALID):
        """ Fills last name input with provided info """
        self.enter_text(self.last_name_input, last_name)

    def enter_checkout_postcode(self,
                                postcode=checkout_info.POSTCODE_VALID):
        """ Fills postcode input with provided info """
        self.enter_text(self.postal_code_input, postcode)

    def click_continue_button(self):
        """ Clicks 'Continue' button to move to next checkout step """
        self.click_element(self.continue_button)

    def click_cancel_button(self):
        """ Clicks 'Cancel' button to stop checkout process """
        self.click_element(self.cancel_button)

    def fill_checkout_info_and_proceed(
            self,
            first_name=checkout_info.FIRST_NAME_VALID,
            last_name=checkout_info.LAST_NAME_VALID,
            postcode=checkout_info.POSTCODE_VALID):
        """ Fills all info fields with provided data (valid by default) and
            clicks 'Continue' """
        self.enter_checkout_first_name(first_name)
        self.enter_checkout_last_name(last_name)
        self.enter_checkout_postcode(postcode)
        self.click_continue_button()

    def get_error_text(self):
        """ Returns text inside error container """
        return self.get_text(self.error_text)

    def get_amount_of_error_icons(self):
        """ Returns amount of error icons displayed """
        return len(self.find_elements(self.error_icons))
