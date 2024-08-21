"""
This module contains the Product page and item page,
which provides functionalities specific to the
products page of the application. Functionality
"Add to card" and "Back to products"
"""

import logging
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
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
        self.add_to_cart_products = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        self.remove_products = (By.ID, "remove-sauce-labs-bolt-t-shirt")

    def get_burger_menu(self):
        return self.find_element(EC.presence_of_element_located
                                 (self.burger_menu))

    def get_title(self):
        return self.find_element(EC.presence_of_element_located
                                 (self.title))

    def get_filter(self):
        return self.find_element(EC.presence_of_element_located
                                 (self.filter))

    def get_card(self):
        return self.find_element(EC.presence_of_element_located
                                 (self.card))

    def get_img_products(self):
        return self.find_element(EC.presence_of_element_located
                                 (self.img_products))

    def get_back_to_products_button(self):
        return self.find_element(EC.presence_of_element_located
                                 (self.back_to_products))

    def get_product_image(self):
        return self.find_element(EC.presence_of_element_located
                                 (self.img))

    def get_product_name(self):
        return self.find_element(EC.presence_of_element_located
                                 (self.product_name))

    def get_product_description(self):
        return self.find_element(EC.presence_of_element_located
                                 (self.description))

    def get_product_price(self):
        return self.find_element(EC.presence_of_element_located
                                 (self.price))

    def get_add_to_cart_button(self):
        return self.find_element(EC.presence_of_element_located
                                 (self.add_to_cart))

    def get_all_items_link(self):
        return self.find_element(EC.presence_of_element_located
                                 (self.all_team))

    def get_card_title(self):
        return self.find_element(EC.presence_of_element_located
                                 (self.card_title))

    def get_card_description(self):
        return self.find_element(EC.presence_of_element_located
                                 (self.card_description))

    def get_card_price(self):
        return self.find_element(EC.presence_of_element_located
                                 (self.card_price))

    def get_add_to_cart_products(self):
        return self.find_element(EC.presence_of_element_located
                                 (self.add_to_cart_products))

    def get_remove_products(self):
        return self.find_element(EC.presence_of_element_located
                                 (self.remove_products))


def check_element(page, element_locator, element_name):
    logging.info(f"Checking for {element_name}")
    element = page.find_element(EC.presence_of_element_located(element_locator))
    assert element.is_displayed(), f"{element_name} not found"
    logging.info(f"{element_name} found")


@pytest.mark.page_elements
@pytest.mark.smoke
def test_page_elements_products_page(product_item_page):
    logging.info("ТС05. Basic elements existance on Products page")

    try:
        check_element(product_item_page,
                      product_item_page.burger_menu, "Burger menu")
        check_element(product_item_page,
                      product_item_page.title, "Title")
        check_element(product_item_page,
                      product_item_page.card, "Card")
        check_element(product_item_page,
                      product_item_page.filter, "~Filter")

        logging.info("Products page has all necessary elements")
        logging.info("Test passed successfully")

    except Exception as e:
        logging.error(f"Test failed: {e}")
        raise e


@pytest.mark.page_elements
@pytest.mark.smoke
def test_page_elements_products_page_item(product_item_page):
    logging.info("ТС06. Basic elements existance on Products page")

    try:
        check_element(product_item_page,
                      product_item_page.img_products, "IMG products")
        check_element(product_item_page,
                      product_item_page.card_title, "Card title")
        check_element(product_item_page,
                      product_item_page.card_description, "Card description")
        check_element(product_item_page,
                      product_item_page.card_price, "Card price")
        check_element(product_item_page,
                      product_item_page.add_to_cart_products, "Add to cart products")

        logging.info("Products page has all necessary elements")
        logging.info("Test passed successfully")

    except Exception as e:
        logging.error(f"Test failed: {e}")
        raise e


def test_add_to_cart_button_products(driver):
    """Step 1: Go to specific product page"""
    logging.info("ТС07. 'Add to card' functionality via 'Products' page")

    try:
        # Step 2: Find and click on the "add-to-cart" button
        logging.info("Attempting to find and click on 'add-to-cart' button")
        add_to_cart_products = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"))
        )
        add_to_cart_products.click()
        logging.info("Clicked on 'add-to-cart' button successfully")

        # Step 3: Make sure the "remove" button appears
        logging.info("Waiting for 'remove' button to appear")
        remove_products = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "remove-sauce-labs-bolt-t-shirt"))
        )
        assert remove_products.is_displayed(), \
            "Expected 'remove' button to be visible after adding item to cart"
        logging.info("'remove' button appeared successfully")

    except TimeoutException as e:
        logging.error("Either 'add-to-cart' button "
                      "was not clickable or 'remove' button did not appear")
        raise e


@pytest.mark.page_elements
@pytest.mark.smoke
def test_page_elements(product_item_page):
    logging.info("ТС08. Basic elements existance on Product item page")

    try:
        check_element(product_item_page,
                      product_item_page.burger_menu, "Burger menu")
        check_element(product_item_page,
                      product_item_page.back_to_products, "Back to Products button")
        check_element(product_item_page,
                      product_item_page.img, "Product image")
        check_element(product_item_page,
                      product_item_page.product_name, "Product name")
        check_element(product_item_page,
                      product_item_page.description, "Product description")
        check_element(product_item_page,
                      product_item_page.price, "Product price")
        check_element(product_item_page,
                      product_item_page.add_to_cart, "Add to Cart button")

        logging.info("Product item page has all necessary elements")
        logging.info("Test passed successfully")

    except Exception as e:
        logging.error(f"Test failed: {e}")
        raise e


def test_add_to_cart_button(driver):
    """Step 1: Go to specific product page"""
    product_url = "https://www.saucedemo.com/inventory-item.html?id=5"
    logging.info(f"ТС09. 'Add to card' functionality via 'Product item' page "
                 f"Navigating to product page: {product_url}")
    driver.get(product_url)

    try:
        # Step 2: Find and click on the "add-to-cart" button
        logging.info("Attempting to find and click on 'add-to-cart' button")
        add_to_cart_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "add-to-cart"))
        )
        add_to_cart_button.click()
        logging.info("Clicked on 'add-to-cart' button successfully")

        # Step 3: Make sure the "remove" button appears
        logging.info("Waiting for 'remove' button to appear")
        remove_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "remove"))
        )
        assert remove_button.is_displayed(), \
            "Expected 'remove' button to be visible after adding item to cart"
        logging.info("'remove' button appeared successfully")

    except TimeoutException as e:
        logging.error("Either 'add-to-cart' button "
                      "was not clickable or 'remove' button did not appear")
        raise e


def test_back_to_products_button(driver):
    """Step 1: Go to specific product page"""
    product_url = "https://www.saucedemo.com/inventory-item.html?id=5"
    logging.info(f"TC10. 'Back to products' functionality. "
                 f"Navigating to product page: {product_url}")
    driver.get(product_url)

    try:
        # Step 2: Make sure the element is clickable and click on it
        logging.info("Attempting to find and click on "
                     "'back-to-products' button")
        back_button_clickable = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "back-to-products"))
        )
        back_button_clickable.click()
        logging.info("Clicked on 'back-to-products' button successfully")

        # Step 3: Make sure the browser is redirected
        # to the product catalog page
        logging.info("Verifying that the browser is "
                     "redirected to the product catalog page")
        WebDriverWait(driver, 20).until(
            EC.url_to_be("https://www.saucedemo.com/inventory.html")
        )
        logging.info("Successfully redirected to the product catalog page")

    except TimeoutException as e:
        logging.error("Element 'back-to-products' not found or not clickable")
        raise e


def test_back_to_products_burger_all_item_button(driver):
    """Step 1: Go to specific product page"""
    product_url = "https://www.saucedemo.com/inventory-item.html?id=5"
    logging.info(f"TC11. 'Back to products via Burger' functionality. "
                 f"Navigating to product page: {product_url}")
    driver.get(product_url)

    try:
        # Step 2: Open burger menu
        logging.info("Attempting to open the burger menu")
        burger_menu_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "react-burger-menu-btn"))
        )
        burger_menu_button.click()
        logging.info("Burger menu opened successfully")

        # Step 3: Find and click on 'all_item' button in the burger menu
        logging.info("Attempting to find and click on 'all_item' button")
        all_item_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "inventory_sidebar_link"))
        )
        all_item_button.click()
        logging.info("Clicked on 'all_item' button successfully")

        # Step 4: Verify that the browser is redirected to the product catalog page
        logging.info("Verifying that the browser is "
                     "redirected to the product catalog page")
        WebDriverWait(driver, 20).until(
            EC.url_to_be("https://www.saucedemo.com/inventory.html")
        )
        logging.info("Successfully redirected to the product catalog page")

    except TimeoutException as e:
        logging.error("Element 'all_item' not found or not clickable")
        raise e
