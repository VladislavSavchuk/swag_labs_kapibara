"""
This module contains the Product item page class,
which provides functionalities specific to the
products page of the application.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductItemPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def get_burger_menu(self):
        return self.wait.until(EC.presence_of_element_located
                               ((By.ID, "react-burger-menu-btn")))

    def get_back_to_products_button(self):
        return self.wait.until(EC.presence_of_element_located
                               ((By.ID, "back-to-products")))

    def get_product_image(self):
        return self.wait.until(EC.presence_of_element_located
                               ((By.CLASS_NAME, "inventory_details_img")))

    def get_product_name(self):
        return self.wait.until(EC.presence_of_element_located
                               ((By.CLASS_NAME, "inventory_details_name")))

    def get_product_description(self):
        return self.wait.until(EC.presence_of_element_located
                               ((By.CLASS_NAME, "inventory_details_desc")))

    def get_product_price(self):
        return self.wait.until(EC.presence_of_element_located
                               ((By.CLASS_NAME, "inventory_details_price")))

    def get_add_to_cart_button(self):
        return self.wait.until(EC.presence_of_element_located
                               ((By.ID, "add-to-cart-sauce-labs-onesie")))

    def get_all_items_link(self):
        return self.wait.until(EC.presence_of_element_located
                               ((By.ID, "inventory_sidebar_link")))
