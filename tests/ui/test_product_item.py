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
from pages.product_item_page import ProductItemPage
from test_data.ui import page_titles, constants, other_text_data


@pytest.mark.product_page
@pytest.mark.smoke
@pytest.mark.uitests
def test_product_item_page_elements(driver):
    logging.info("TC08. Basic elements existence on Product item page")
    login_page = LoginPage(driver)
    all_products_page = AllProductsPage(driver)
    product_item_page = ProductItemPage(driver)

    login_page.login()
    all_products_page.open_random_product_item()

    product_item_page.check_page_elements()
    logging.info("Product item page has all necessary elements. "
                 "Test passed successfully")


@pytest.mark.product_page
@pytest.mark.smoke
@pytest.mark.uitests
def test_add_to_cart_button(driver):
    logging.info("TC09. 'Add to card' functionality via 'Product item' page")
    login_page = LoginPage(driver)
    all_products_page = AllProductsPage(driver)
    product_item_page = ProductItemPage(driver)

    login_page.login()
    all_products_page.open_random_product_item()

    product_item_page.click_add_to_cart()
    assert product_item_page.get_remove_button()
    logging.info("'Remove' button appeared successfully")


@pytest.mark.product_page
@pytest.mark.smoke
@pytest.mark.uitests
def test_back_to_products_button(driver):
    logging.info("TC10. 'Back to products' functionality.")
    login_page = LoginPage(driver)
    all_products_page = AllProductsPage(driver)
    product_item_page = ProductItemPage(driver)

    login_page.login()
    all_products_page.open_random_product_item()

    product_item_page.open_burger_menu()
    product_item_page.click_back_to_products_button()

    assert all_products_page.get_page_title() == page_titles.ALL_PRODUCTS
    logging.info("Successfully redirected to the product catalog page")


@pytest.mark.product_page
@pytest.mark.smoke
@pytest.mark.uitests
def test_burger_all_item_button(driver):
    logging.info("TC11. 'Back to products via Burger' functionality")
    login_page = LoginPage(driver)
    all_products_page = AllProductsPage(driver)
    product_item_page = ProductItemPage(driver)

    login_page.login()
    all_products_page.open_random_product_item()

    product_item_page.open_burger_menu()
    product_item_page.click_all_items_burger_button()

    assert all_products_page.get_page_title() == page_titles.ALL_PRODUCTS
    logging.info("Successfully redirected to the product catalog page")


@pytest.mark.xfail
@pytest.mark.product_page
@pytest.mark.smoke
@pytest.mark.uitests
def test_invalid_url_product(driver):
    logging.info("TC08(neg). Changing product id to invalid value via URL")
    login_page = LoginPage(driver)
    product_item_page = ProductItemPage(driver)

    login_page.login()

    driver.get(constants.INVALID_PRODUCT_URL)

    assert (product_item_page.get_product_title_text() ==
            other_text_data.ITEM_NOT_FOUND_TITLE)
    logging.info("Page title of 'Item not found' page is correct")
    assert (product_item_page.get_product_title_description() ==
            other_text_data.ITEM_NOT_FOUND_DESCRIPTION)
    logging.info("Page description of 'Item not found' page is correct")

    assert product_item_page.get_add_to_cart_button is TimeoutError, "'Add "\
        "to cart' button should not be present at 'Item not found' page"
