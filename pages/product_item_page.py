"""
This module contains the Product page and item page,
which provides functionalities specific to the
products page of the application. Functionality
"Add to card" and "Back to products"
"""

import logging
import pytest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from pages.login_page import LoginPage
from pages.base import BasePage


@pytest.fixture
def product_item_page(driver):
    """
    Fixture to log in and return the ProductItemPage instance
    """
    logging.info("Logging in to access the product item page")
    login_page = LoginPage(driver)
    login_page.login()
    return ProductItemPage(driver)


class ProductItemPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.burger_menu = (By.ID, "react-burger-menu-btn")
        self.all_items = (By.ID, "inventory_sidebar_link")

        self.back_to_products = (By.ID, "back-to-products")
        self.add_to_cart_button = (By.ID, "add-to-cart")

        self.product_image = (By.CLASS_NAME, "inventory_details_img")
        self.product_title = (
            By.CSS_SELECTOR, "[data-test='inventory-item-name']")
        self.product_description = (
            By.CSS_SELECTOR, "[data-test='inventory-item-desc']")
        self.product_price = (By.CLASS_NAME, "inventory_details_price")
        self.product_add_to_cart = (By.ID, "add-to-cart")
        self.products_remove = (By.ID, "remove")

    def get_product_title_text(self):
        """Returns product title text"""
        return self.get_text(self.product_title)

    def get_product_title_description(self):
        """Returns product description text"""
        return self.get_text(self.product_description)

    def click_add_to_cart(self):
        """ Clicks 'Add to Cart' button """
        return self.click_element(self.add_to_cart_button)

    def open_burger_menu(self):
        """ Opens burger menu """
        return self.click_element(self.burger_menu)

    def click_all_items_burger_button(self):
        """ Clicks at 'All Items' button at burger menu if found """
        self.click_element(self.all_items)

    def click_back_to_products_button(self):
        """ Clicks at 'Back to products' button at burger menu if found """
        self.click_element(self.back_to_products)

    def get_add_to_cart_button(self):
        """ Returns remove button if its found """
        return self.find_element(self.add_to_cart_button)

    def get_remove_button(self):
        """ Returns remove button if its found """
        return self.find_element(self.products_remove)

    def check_page_elements(self):
        """ Finds elements on the page, returns False otherwise """
        elements = [self.burger_menu,
                    self.product_image,
                    self.product_title,
                    self.product_description,
                    self.product_price,
                    self.product_add_to_cart,
                    self.back_to_products]
        try:
            for element in elements:
                self.find_element(element)

        except TimeoutException:
            return False
        return True
