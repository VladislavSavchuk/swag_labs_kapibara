"""
Testing the products page of saucedemo.com.

This module contains a set of tests to check the presence
of Basic elements existence on "Product item" page
"""


import logging
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.login_page import LoginPage
from pages.product_item_page import ProductItemPage


@pytest.fixture
def driver():
    service = Service(executable_path='/usr/local/bin/chromedriver')
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.saucedemo.com/inventory-item.html?id=5")
    yield driver
    driver.quit()


@pytest.fixture
def product_item_page(driver):
    """
    Fixture to log in and return the ProductItemPage instance
    """
    logging.info("Logging in to access the product item page")
    login_page = LoginPage(driver)
    login_page.login()
    return ProductItemPage(driver)


@pytest.mark.page_elements
@pytest.mark.smoke
def test_page_elements(driver):
    logging.info("Starting test_page_elements")

    page = ProductItemPage(driver)

    try:
        # 1.1 Burger menu
        logging.info("Checking for Burger menu")
        burger_menu = page.get_burger_menu()
        assert burger_menu.is_displayed(), "Burger menu not found"
        logging.info("Burger menu found")

        # 1.2 Page title
        # logging.info("Checking for Page title")
        # page_title = driver.title
        # assert "Sauce Labs Onesie" in page_title,
        # f"Incorrect page title: {page_title}"
        # logging.info(f"Page title is correct: {page_title}")

        # 1.3 Back to products button
        logging.info("Checking for Back to Products button")
        back_to_products_button = page.get_back_to_products_button()
        assert back_to_products_button.is_displayed(), \
            "Back to Products button not found"
        logging.info("Back to Products button found")

        # 1.4 Product image
        logging.info("Checking for Product image")
        product_image = page.get_product_image()
        assert product_image.is_displayed(), "Product image not found"
        logging.info("Product image found")

        # 1.5 Product name
        logging.info("Checking for Product name")
        product_name = page.get_product_name()
        assert product_name.is_displayed(), "Product name not found"
        logging.info("Product name found")

        # 1.6 Product description
        logging.info("Checking for Product description")
        product_description = page.get_product_description()
        assert product_description.is_displayed(), \
            "Product description not found"
        logging.info("Product description found")

        # 1.7 Product price
        logging.info("Checking for Product price")
        product_price = page.get_product_price()
        assert product_price.is_displayed(), "Product price not found"
        logging.info("Product price found")

        # 1.8 Add to Cart button
        logging.info("Checking for Add to Cart button")
        add_to_cart_button = page.get_add_to_cart_button()
        assert add_to_cart_button.is_displayed(), \
            "Add to Cart button not found"
        logging.info("Add to Cart button found")

        logging.info("Test passed successfully")

    except Exception as e:
        logging.error(f"Test failed: {e}")
        raise e
