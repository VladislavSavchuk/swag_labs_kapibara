"""
This module contains the AllProductsPage class, which provides functionalities
specific to the products page of the application.
"""

from selenium.webdriver.common.by import By
from pages.base import BasePage


class AllProductsPage(BasePage):
    """
    Class representing the products page of the application.
    Inherits from BasePage to provide common page functionalities.
    """

    def __init__(self, driver):
        """
        Initializes the AllProductsPage with the provided WebDriver instance
        and sets up the locators for the login page elements.

        Parameters:
            driver (selenium.webdriver.remote.webdriver.WebDriver):
                The WebDriver instance used to interact with the browser.
        """
        super().__init__(driver)
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
