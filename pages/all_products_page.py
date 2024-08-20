"""
This module contains the AllProductsPage class, which provides functionalities
specific to the products page of the application.
"""

import logging
from random import randrange
from selenium.webdriver.common.by import By
from pages.base import BasePage


class AllProductsPage(BasePage):
    """
    Class representing the products page of the application.
    """

    def __init__(self, driver):
        """
        Initializes AllProductsPage and sets up the locators and methods for
        products page.
        """
        super().__init__(driver)
        self.page_title = (By.CLASS_NAME, "title")

        self.inventory_list = (By.CLASS_NAME, "inventory_list")
        self.cart_button = (By.CLASS_NAME, "shopping_cart_link")
        self.cart_badge = (By.CLASS_NAME, "shopping_cart_badge")

        self.sorting_selector = (
            By.XPATH, "//select[@data-test='product-sort-container']")
        self.active_sorting_option = (By.CLASS_NAME, "active_option")
        self.sorting_options = (By.TAG_NAME, "option")
        self.sorting_abc_asc = (By.XPATH, "//option[@value='az']")
        self.sorting_abc_desc = (By.XPATH, "//option[@value='za']")
        self.sorting_price_asc = (By.XPATH, "//option[@value='lohi']")
        self.sorting_price_desc = (By.XPATH, "//option[@value='hilo']")

        self.product_title = (By.CLASS_NAME, "inventory_item_name ")
        self.product_price = (By.CLASS_NAME, "inventory_item_price")
        self.add_to_cart_button = (By.ID, "add-to-cart-sauce-labs-onesie")

    def get_page_title(self):
        """ Returns page title text """
        return self.get_text(self.page_title)

    def check_products_exist(self):
        """ Returns elements if found, TimeoutException otherwise """
        return self.find_element(self.inventory_list)

    def get_active_sorting_option_text(self):
        """ Returns text of active sorting option """
        return self.get_text(self.active_sorting_option)

    def click_sorting_selector(self):
        """ Clicks on sorting selector to show available options """
        self.click_element(self.sorting_selector)

    def select_sorting_option(self, option):
        """ Opens dropdown and selects specified sorting option """
        self.click_element(self.sorting_selector)
        self.click_element(option)

    def get_all_sorting_options_text(self):
        """ Returns list containing text of all sorting options """
        return self.get_all_elements_texts(self.sorting_options)

    def get_all_products_titles(self):
        """ Returns list of all products titles in order they're displayed
            on the page """
        return self.get_all_elements_texts(self.product_title)

    def get_all_products_prices(self):
        """ Returns list of all products prices without currency symbol and in
            numeric format in same order they're displayed on the page """
        prices = self.get_all_elements_texts(self.product_price)
        prices = [float(elem.replace('$', '')) for elem in prices]
        return prices

    def add_random_product_to_cart(self):
        """ Clicks 'Add to cart' on random product """
        add_buttons_list = self.find_elements(self.add_to_cart_button)
        self.click_element(add_buttons_list[randrange(len(add_buttons_list))])

        assert self.cart_badge_number() == '1'
        logging.info("1 product added to cart")

    def cart_badge_number(self):
        """ Returns the number at cart badge representing amount of products
            added to cart """
        return self.get_text(self.cart_badge)

    def go_to_cart(self):
        """ Clicks at cart button """
        self.click_element(self.cart_button)
