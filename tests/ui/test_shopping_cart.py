"""
Testing the shopping cart functionality of saucedemo.com.

This module contains a suite of tests to verify the shopping cart
functionality of the saucedemo.com website. Each test checks different
buttons on the shopping cart page: add to cart, remove item, continue
shopping and verify presence of elements.
"""

import logging
import pytest
from pages.login_page import LoginPage
from pages.shopping_cart_page import ShoppingCartPage
from pages.all_products_page import AllProductsPage


@pytest.mark.shopping_cart
@pytest.mark.smoke
@pytest.mark.uitests
def test_verify_presence_elements_on_cart_page(driver):
    """
    This test verifies that the shopping cart page has all necessary
    elements of the product card:
    name, description, price, qty, and remove button.
    """
    logging.info("TC16: Verify that product card has all necessary elements")

    login_page = LoginPage(driver)
    shopping_cart_page = ShoppingCartPage(driver)

    # Log in and navigate to cart page
    login_page.login()
    shopping_cart_page.click_add_to_cart_btn()
    shopping_cart_page.click_shop_icon()

    # Verify elements
    shopping_cart_page.verify_presence_elements_on_cart_page()

    logging.info("Shopping cart page has all necessary elements")


@pytest.mark.shopping_cart
@pytest.mark.smoke
@pytest.mark.uitests
def test_remove_item_from_cart(driver):
    """
    This test verifies that a user can remove
    an item from the shopping cart.
    """
    logging.info("TC17: Verify remove an item from the shopping cart")

    login_page = LoginPage(driver)
    shopping_cart_page = ShoppingCartPage(driver)

    # Log in and navigate to cart page
    login_page.login()
    shopping_cart_page.click_add_to_cart_btn()
    shopping_cart_page.click_shop_icon()

    # Remove item
    shopping_cart_page.click_remove_item_btn()

    # Verify item is removed
    assert shopping_cart_page.verify_remove_item_from_cart()

    logging.info("Item was removed from cart")


@pytest.mark.shopping_cart
@pytest.mark.smoke
@pytest.mark.uitests
def test_return_to_shopping_from_cart(driver):
    """
    This test verifies that a user can continue shopping.
    """
    logging.info("TC18: Verify that a user can continue shopping")

    login_page = LoginPage(driver)
    shopping_cart_page = ShoppingCartPage(driver)
    all_products_page = AllProductsPage(driver)

    # Log in and navigate to cart page
    login_page.login()
    shopping_cart_page.click_shop_icon()

    # Return to shopping
    shopping_cart_page.click_continue_shopping_btn()

    # Verify that user is redirected to all products page
    assert all_products_page.get_all_products_titles()

    logging.info("User is redirected to all products page")
