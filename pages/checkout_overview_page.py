"""
This module contains the CheckoutOverviewPage class, which provides
functionalities specific to the 'Checkout: Overview' page of the
application.
"""

from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from pages.base import BasePage


class CheckoutOverviewPage(BasePage):
    """
    Class representing the 'Checkout: Overview' page of the
    application.
    """

    def __init__(self, driver):
        """
        Initializes CheckoutOverviewPage and sets up locators and methods for
        'Checkout: Overview' page.
        """
        super().__init__(driver)
        self.page_title = (By.CLASS_NAME, "title")

        self.product_cart = (By.CLASS_NAME, "cart_item")
        self.product_quantity = (By.CLASS_NAME, "cart_quantity")
        self.product_title = (By.CLASS_NAME, "inventory_item_name")
        self.product_description = (By.CLASS_NAME, "inventory_item_desc")
        self.product_price = (By.CLASS_NAME, "inventory_item_price")
        self.payment_info_section = (By.CSS_SELECTOR,
                                     "[data-test='payment-info-label']")
        self.payment_card_info = (By.CSS_SELECTOR,
                                  "[data-test='payment-info-value']")
        self.shipping_info_section = (By.CSS_SELECTOR,
                                      "[data-test='shipping-info-label']")
        self.shipping_company_info = (By.CSS_SELECTOR,
                                      "[data-test='shipping-info-value']")
        self.price_total_section = (By.CSS_SELECTOR,
                                    "[data-test='total-info-label']")
        self.items_total_price = (By.CSS_SELECTOR,
                                  "[data-test='subtotal-label']")
        self.taxes_price = (By.CSS_SELECTOR, "[data-test='tax-label']")
        self.total_price = (By.CSS_SELECTOR, "[data-test='total-label']")

        self.cancel_button = (By.ID, "cancel")
        self.finish_button = (By.ID, "finish")

    def get_page_title(self):
        """ Returns page title text """
        return self.get_text(self.page_title)

    def check_page_elements(self):
        """ Finds inputs for user info, returns False otherwise """
        try:
            self.find_element(self.product_cart)
            self.find_element(self.product_quantity)
            self.find_element(self.product_title)
            self.find_element(self.product_description)
            self.find_element(self.product_price)
            self.find_element(self.payment_info_section)
            self.find_element(self.payment_card_info)
            self.find_element(self.shipping_info_section)
            self.find_element(self.shipping_company_info)
            self.find_element(self.price_total_section)
            self.find_element(self.items_total_price)
            self.find_element(self.taxes_price)
            self.find_element(self.total_price)
            self.find_element(self.cancel_button)
            self.find_element(self.finish_button)
        except TimeoutException:
            return False
        return True

    def check_taxes_calculated(self):
        """ Calculates the taxes and compares with number at the page"""
        items_total = float(self.get_text(self.items_total_price)
                                .replace('Item total: $', ''))
        taxes = float(self.get_text(self.taxes_price)
                          .replace('Tax: $', ''))
        taxes_calc = round((items_total * 0.08), 2)
        return taxes_calc == taxes

    def check_total_amount_calculated(self):
        """ Calculates the total sum based on items amount and 8% taxes """
        items_total = float(self.get_text(self.items_total_price)
                                .replace('Item total: $', ''))
        total = float(self.get_text(self.total_price)
                          .replace('Total: $', ''))
        total_calc = round((items_total * 1.08), 2)
        return total_calc == total

    def click_finish(self):
        """ Clicks 'Finish' button to place the order """
        self.click_element(self.finish_button)
