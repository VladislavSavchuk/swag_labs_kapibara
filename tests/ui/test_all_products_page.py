"""
This module contains the Product page and item page,
which provides functionalities specific to the
products page of the application. Functionality
"Add to card" and "Back to products"
"""

import logging
import pytest
from pages.login_page import LoginPage
from pages.all_products_page import AllProductsPage


@pytest.mark.all_products_page
@pytest.mark.smoke
@pytest.mark.uitests
def test_page_elements_all_products_page(driver):
    logging.info("TC05. Basic elements existence on All Products page")
    login_page = LoginPage(driver)
    all_products_page = AllProductsPage(driver)

    login_page.login()

    assert all_products_page.check_page_elements()
    logging.info("All Products page has all necessary elements")


@pytest.mark.all_products_page
@pytest.mark.smoke
@pytest.mark.uitests
def test_page_elements_products_page_item(driver):
    logging.info("TC06. Basic elements existence on Products card")
    login_page = LoginPage(driver)
    all_products_page = AllProductsPage(driver)

    login_page.login()
    assert all_products_page.check_inventory_list_elements()
    logging.info("Product card has all necessary elements")


@pytest.mark.all_products_page
@pytest.mark.smoke
@pytest.mark.uitests
def test_add_to_cart_button_products(driver):
    logging.info("TC07. 'Add to card' functionality via 'Products' page")
    login_page = LoginPage(driver)
    all_products_page = AllProductsPage(driver)

    login_page.login()

    all_products_page.add_random_product_to_cart()
    logging.info("Clicked on 'add-to-cart' button successfully")

    all_products_page.get_remove_button()
    logging.info("'Remove' button appeared successfully")
