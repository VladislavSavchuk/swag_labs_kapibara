"""
This module contains the CartPage class, which provides functionalities
specific to the cart page of the application.
"""

import logging
from selenium.webdriver.common.by import By
from pages.base import BasePage


class CartPage(BasePage):
    """
    Class representing the cart page of the application.
    """

    def __init__(self, driver):
        """
        Initializes CartPage and sets up locators and methods for cart page.
        """
        super().__init__(driver)
        self.page_title = (By.CLASS_NAME, "title")

        self.cart_list = (By.CLASS_NAME, "cart_list")
        self.cart_items = (By.CLASS_NAME, "cart_item")
        self.product_titles_list = (By.CLASS_NAME, "inventory_item_name")
        self.checkout_button = (By.ID, "checkout")

    def get_page_title(self):
        """ Returns page title text """
        return self.get_text(self.page_title)

    def check_cart_items_exists(self):
        """ Returns elements if found, TimeoutException otherwise """
        return self.find_element(self.cart_items)

    def click_checkout_button(self):
        """ Clicks checkout button """
        self.click_element(self.checkout_button)
        logging.info("Checkout started")
