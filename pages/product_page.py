"""
This module contains the Product page and item page,
which provides functionalities specific to the
products page of the application. Functionality
"Add to card" and "Back to products"
"""

import logging
import pytest
from selenium.webdriver.common.by import By
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
        self.title = (By.CLASS_NAME, "app_logo")
        self.filter = (By.CLASS_NAME, "product_sort_container")
        self.card = (By.CLASS_NAME, "inventory_item_desc")
        self.back_to_products = (By.ID, "back-to-products")
        self.img_products = (By.CLASS_NAME, "inventory_item_img")
        self.img = (By.CLASS_NAME, "inventory_details_img")
        self.product_name = (By.CLASS_NAME, "inventory_details_name")
        self.description = (By.CLASS_NAME, "inventory_details_desc")
        self.price = (By.CLASS_NAME, "inventory_details_price")
        self.add_to_cart = (By.ID, "add-to-cart")
        self.all_team = (By.ID, "inventory_sidebar_link")
        self.card_title = (By.CLASS_NAME, "inventory_item_name")
        self.card_description = (By.CLASS_NAME, "inventory_item_desc")
        self.card_price = (By.CLASS_NAME, "inventory_item_price")
        self.add_to_cart_products = (By.ID,
                                     "add-to-cart-sauce-labs-bolt-t-shirt")
        self.remove_products = (By.ID, "remove-sauce-labs-bolt-t-shirt")

    def get_burger_menu(self):
        return self.find_element(self.burger_menu)

    def get_title(self):
        return self.find_element(self.title)

    def get_filter(self):
        return self.find_element(self.filter)

    def get_card(self):
        return self.find_element(self.card)

    def get_img_products(self):
        return self.find_element(self.img_products)

    def get_back_to_products_button(self):
        return self.find_element(self.back_to_products)

    def get_product_image(self):
        return self.find_element(self.img)

    def get_product_name(self):
        return self.find_element(self.product_name)

    def get_product_description(self):
        return self.find_element(self.description)

    def get_product_price(self):
        return self.find_element(self.price)

    def get_add_to_cart_button(self):
        return self.find_element(self.add_to_cart)

    def get_all_items_link(self):
        return self.find_element(self.all_team)

    def get_card_title(self):
        return self.find_element(self.card_title)

    def get_card_description(self):
        return self.find_element(self.card_description)

    def get_card_price(self):
        return self.find_element(self.card_price)

    def get_add_to_cart_products(self):
        return self.find_element(self.add_to_cart_products)

    def get_remove_products(self):
        return self.find_element(self.remove_products)


def check_element(page, element_locator, element_name):
    logging.info(f"Checking for {element_name}")
    element = page.find_element(element_locator)
    assert element.is_displayed(), f"{element_name} not found"
    logging.info(f"{element_name} found")
