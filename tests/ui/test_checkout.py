"""
Testing the checkout functionality of saucedemo.com.

This module contains a suite of tests to verify the checkout process and
related functionalities of the saucedemo.com website.
"""

import logging
import pytest

from pages.login_page import LoginPage
from pages.all_products_page import AllProductsPage
from pages.cart_page import CartPage
from pages.checkout_info_page import CheckoutInfoPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.checkout_complete_page import CheckoutCompletePage

from test_data.ui import (page_titles)
from test_data.ui import checkout_info, errors_text, other_text_data


@pytest.mark.checkout
@pytest.mark.smoke
@pytest.mark.uitests
def test_start_checkout(driver):
    """
    Test ability to start checkout process.

    This test verifies that user can click 'Checkout' button at cart page and
    be redirected to "Checkout: Your information" page after it.
    """
    logging.info("TC19. Verify that user can start checkout process by "
                 "clicking 'Checkout' at cart page")

    login_page = LoginPage(driver)
    all_products_page = AllProductsPage(driver)
    cart_page = CartPage(driver)
    checkout_info_page = CheckoutInfoPage(driver)
    login_page.login()

    all_products_page.check_products_exist()
    all_products_page.add_random_product_to_cart()
    all_products_page.go_to_cart()

    cart_page.check_cart_items_exists()
    cart_page.click_checkout_button()

    assert checkout_info_page.get_page_title() == page_titles.CHECKOUT_INFO
    logging.info("User successfully redirected to 'Checkout: Your "
                 "information' page")

    assert checkout_info_page.check_page_elements()
    logging.info("'Checkout: Your information' page has First Name, Last Name "
                 "and postcode inputs, 'Cancel' button and 'Continue' button")


@pytest.mark.checkout
@pytest.mark.smoke
@pytest.mark.uitests
def test_enter_valid_checkout_info(driver):
    """
    Test ability to process valid checkout info.

    This test verifies that user can enter valid checkout info, click
    'Continue' and be redirected to "Checkout: Overview" page after it.
    """
    logging.info("TC20. Verify that user can enter valid checkout info and "
                 "get to 'Overview' page")

    login_page = LoginPage(driver)
    all_products_page = AllProductsPage(driver)
    cart_page = CartPage(driver)
    checkout_info_page = CheckoutInfoPage(driver)
    checkout_overview_page = CheckoutOverviewPage(driver)
    login_page.login()

    all_products_page.check_products_exist()
    all_products_page.add_random_product_to_cart()
    all_products_page.go_to_cart()

    cart_page.check_cart_items_exists()
    cart_page.click_checkout_button()

    checkout_info_page.enter_checkout_first_name()
    checkout_info_page.enter_checkout_last_name()
    checkout_info_page.enter_checkout_postcode()
    checkout_info_page.click_continue_button()

    assert (checkout_overview_page.get_page_title() ==
            page_titles.CHECKOUT_OVERVIEW)
    logging.info("User successfully redirected to 'Checkout: Overview page")

    assert checkout_overview_page.check_page_elements()
    logging.info("'Checkout: Overview' page has product card which include "
                 "product quantity, title, description and price; "
                 "payment info section with payment method info; "
                 "shipping info section with shipping company info; "
                 "price section with total price, taxes and total amount; "
                 "'Cancel' and 'Finish' buttons")


@pytest.mark.checkout
@pytest.mark.smoke
@pytest.mark.uitests
def test_correct_total(driver):
    """
    Test accuracy of tax calculations.

    This test verifies that taxes are 8% and total amount calculated correctly.
    """
    logging.info("TC21. Verify that user can see correct total amount at "
                 "Overview page")

    login_page = LoginPage(driver)
    all_products_page = AllProductsPage(driver)
    cart_page = CartPage(driver)
    checkout_info_page = CheckoutInfoPage(driver)
    checkout_overview_page = CheckoutOverviewPage(driver)
    login_page.login()

    all_products_page.check_products_exist()
    all_products_page.add_random_product_to_cart()
    all_products_page.go_to_cart()

    cart_page.check_cart_items_exists()
    cart_page.click_checkout_button()

    checkout_info_page.fill_checkout_info_and_proceed()

    assert checkout_overview_page.check_taxes_calculated()
    logging.info("Taxes calculated correctly")

    assert checkout_overview_page.check_total_amount_calculated()
    logging.info("Total calculated correctly")


@pytest.mark.checkout
@pytest.mark.smoke
@pytest.mark.uitests
def test_finish_checkout(driver):
    """
    Test possibility to place the order.

    This test verifies that order can be placed by clicking 'Finish' at
    'Checkout: Overview' page.
    """
    logging.info("TC22. Verify that user can place an order by clicking "
                 "'Finish' at 'Overview' page")

    login_page = LoginPage(driver)
    all_products_page = AllProductsPage(driver)
    cart_page = CartPage(driver)
    checkout_info_page = CheckoutInfoPage(driver)
    checkout_overview_page = CheckoutOverviewPage(driver)
    checkout_complete_page = CheckoutCompletePage(driver)
    login_page.login()

    all_products_page.check_products_exist()
    all_products_page.add_random_product_to_cart()
    all_products_page.go_to_cart()

    cart_page.check_cart_items_exists()
    cart_page.click_checkout_button()

    checkout_info_page.fill_checkout_info_and_proceed()

    checkout_overview_page.click_finish()

    assert checkout_complete_page.check_page_elements()
    logging.info("'Checkout: Complete' page has complete icon, title, text "
                 "and 'Back Home' button")

    assert (checkout_complete_page.get_complete_header_text() ==
            other_text_data.COMPLETE_HEADER)
    logging.info("Complete header text is correct")

    assert (checkout_complete_page.get_complete_description_text() ==
            other_text_data.COMPLETE_DESCRIPTION)
    logging.info("Complete description text is correct")


@pytest.mark.checkout
@pytest.mark.smoke
@pytest.mark.uitests
def test_back_home_after_checkout(driver):
    """
    Test possibility to return to All Products page after placing the order.

    This test verifies that user can be returned to Home page after placing
    the order and clicking 'Back Home' button at 'Checkout: Complete!'.
    """
    logging.info("TC23. Verify that user can return to home page after "
                 "placing the order")

    login_page = LoginPage(driver)
    all_products_page = AllProductsPage(driver)
    cart_page = CartPage(driver)
    checkout_info_page = CheckoutInfoPage(driver)
    checkout_overview_page = CheckoutOverviewPage(driver)
    checkout_complete_page = CheckoutCompletePage(driver)
    login_page.login()

    all_products_page.check_products_exist()
    all_products_page.add_random_product_to_cart()
    all_products_page.go_to_cart()

    cart_page.check_cart_items_exists()
    cart_page.click_checkout_button()

    checkout_info_page.fill_checkout_info_and_proceed()

    checkout_overview_page.click_finish()
    checkout_complete_page.click_back_home_button()

    assert all_products_page.get_page_title() == page_titles.ALL_PRODUCTS
    logging.info("User successfully redirected to Products page")


@pytest.mark.checkout
@pytest.mark.smoke
@pytest.mark.uitests
def test_cancel_checkout(driver):
    """
    Test possibility cancel checkout process.

    This test verifies that user can be returned to Home page after cancelling
    checkout via clicking 'Cancel' button at 'Checkout: Your Information' page.
    """
    logging.info("TC24. Verify that user can cancel checkout procedure")

    login_page = LoginPage(driver)
    all_products_page = AllProductsPage(driver)
    cart_page = CartPage(driver)
    checkout_info_page = CheckoutInfoPage(driver)
    login_page.login()

    all_products_page.check_products_exist()
    all_products_page.add_random_product_to_cart()
    all_products_page.go_to_cart()

    cart_page.check_cart_items_exists()
    cart_page.click_checkout_button()

    checkout_info_page.click_cancel_button()
    logging.info("Checkout terminated")

    assert cart_page.get_page_title() == page_titles.CART
    logging.info("User successfully returned to 'Your Cart' page")

    assert cart_page.check_cart_items_exists()
    logging.info("Cart item(s) remain in cart after terminating checkout "
                 "process")


@pytest.mark.xfail
@pytest.mark.checkout
@pytest.mark.smoke
@pytest.mark.uitests
def test_empty_checkout_info(driver):
    """
    Test errors appear after skipping entering checkout info.

    This test verifies that user can see errors appear after clicking
    'Continue' if checkout info is empty.
    """
    logging.info("TC25. Verify that user can see error messages when skipping "
                 "entering checkout info")

    login_page = LoginPage(driver)
    all_products_page = AllProductsPage(driver)
    cart_page = CartPage(driver)
    checkout_info_page = CheckoutInfoPage(driver)
    login_page.login()

    all_products_page.check_products_exist()
    all_products_page.add_random_product_to_cart()
    all_products_page.go_to_cart()

    cart_page.check_cart_items_exists()
    cart_page.click_checkout_button()

    checkout_info_page.click_continue_button()

    assert checkout_info_page.get_amount_of_error_icons() == 3
    logging.info("Number of error indicators corresponds to empty fields")

    assert (errors_text.CHECKOUT_EMPTY_FIRST_NAME +
            errors_text.CHECKOUT_EMPTY_LAST_NAME +
            errors_text.CHECKOUT_EMPTY_POSTCODE in
            checkout_info_page.get_error_text())
    logging.info("Error messages are correct")


@pytest.mark.xfail
@pytest.mark.checkout
@pytest.mark.smoke
@pytest.mark.uitests
def test_invalid_checkout_info(driver):
    """
    Test errors appear after entering invalid checkout info.

    This test verifies that user can see errors appear after clicking
    'Continue' if checkout info is filled with invalid data such as including
    special characters.
    """
    logging.info("TC26. Verify that user can see error messages when entering "
                 "invalid checkout info")

    login_page = LoginPage(driver)
    all_products_page = AllProductsPage(driver)
    cart_page = CartPage(driver)
    checkout_info_page = CheckoutInfoPage(driver)
    login_page.login()

    all_products_page.check_products_exist()
    all_products_page.add_random_product_to_cart()
    all_products_page.go_to_cart()

    cart_page.check_cart_items_exists()
    cart_page.click_checkout_button()

    checkout_info_page.fill_checkout_info_and_proceed(
        checkout_info.FIRST_NAME_INVALID,
        checkout_info.LAST_NAME_INVALID,
        checkout_info.POSTCODE_INVALID)

    checkout_info_page.click_continue_button()

    assert checkout_info_page.get_amount_of_error_icons() == 3
    logging.info("Number of error indicators corresponds to empty fields")

    assert (errors_text.CHECKOUT_INVALID_FIRST_NAME +
            errors_text.CHECKOUT_INVALID_LAST_NAME +
            errors_text.CHECKOUT_INVALID_POSTCODE in
            checkout_info_page.get_error_text())
    logging.info("Error messages are correct")
