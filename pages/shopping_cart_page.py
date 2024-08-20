"""
This module contains the Shopping Cart Page class,
which provides functionalities specific to
the shopping cart page of the application.
"""

import logging
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from pages.base import BasePage


class ShoppingCartPage(BasePage):
    """
    Class representing the shopping cart page of the application.
    Inherits from BasePage to provide common page functionalities.
    """

    def __init__(self, driver):
        """
        Initializes the ShoppingCartPage with the provided WebDriver instance
        and sets up the locators for the shopping cart page elements.
        """
        super().__init__(driver)
        self.add_to_cart_btn = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.shop_icon = (By.ID, "shopping_cart_container")
        self.shop_icon_badge = (By.CLASS_NAME, "shopping_cart_badge")
        self.cart_items_name = (By.CLASS_NAME, "inventory_item_name")
        self.cart_items_desc = (By.CLASS_NAME, "inventory_item_desc")
        self.cart_items_price = (By.CLASS_NAME, "inventory_item_price")
        self.cart_items_qty = (By.CLASS_NAME, "cart_quantity")
        self.remove_item_btn = (By.ID, "remove-sauce-labs-backpack")
        self.checkout_btn = (By.ID, "checkout")
        self.continue_shopping_btn = (By.ID, "continue-shopping")

    def click_add_to_cart_btn(self):
        """ Clicks on add to cart button """
        self.click_element(self.add_to_cart_btn)

    def click_remove_item_btn(self):
        """ Clicks on remove item button """
        self.click_element(self.remove_item_btn)

    def click_continue_shopping_btn(self):
        """ Clicks on continue shopping button """
        self.click_element(self.continue_shopping_btn)

    def click_shop_icon(self):
        """ Clicks on shop icon """
        self.click_element(self.shop_icon)

    def get_shop_icon_badge(self):
        """ Returns shop icon badge """
        return self.get_text(self.shop_icon_badge)

    def get_cart_items_name(self):
        """ Returns cart items name """
        return self.get_text(self.cart_items_name)

    def get_cart_items_desc(self):
        """ Returns cart items description """
        return self.get_text(self.cart_items_desc)

    def get_cart_items_price(self):
        """ Returns cart items price """
        return self.get_text(self.cart_items_price)

    def get_cart_items_qty(self):
        """ Returns cart items quantity """
        return self.get_text(self.cart_items_qty)

    def verify_remove_item_from_cart(self):
        """ Verifies that item was removed from cart """
        try:
            logging.info("Verify that item was removed from cart")

            # Wait for remove button and badge to become invisible
            remove_button_invisible = self.element_is_invisible(
                self.remove_item_btn)
            badge_invisible = self.element_is_invisible(
                self.shop_icon_badge)

            return remove_button_invisible and badge_invisible

        except TimeoutException:
            logging.info("Item was not removed from cart")
            return False

    def verify_presence_elements_on_cart_page(self):
        """ Verifies that all necessary elements are present
        on the shopping cart page """
        # List of elements to check
        elements_to_check = [
            (self.cart_items_name,
             "Product name not found on the cart page"),
            (self.cart_items_desc,
             "Product description not found on the cart page"),
            (self.cart_items_price,
             "Product price not found on the cart page"),
            (self.cart_items_qty,
             "Product quantity not found on the cart page"),
            (self.shop_icon_badge,
             "Shop icon badge not found on the cart page"),
            (self.remove_item_btn,
             "Remove item button not found on the cart page"),
        ]

        try:
            for locator, error_message in elements_to_check:
                self.find_element(locator)

                # Check if locator is shop icon badge
                if locator == self.shop_icon_badge:
                    # Special case for shop icon badge
                    assert self.get_shop_icon_badge() == "1", error_message
                else:
                    # All other elements
                    assert self.get_text(locator), error_message

            logging.info("Shopping cart page has all necessary elements")
        except Exception as e:
            logging.error(f"Error: {str(e)}")
            raise
