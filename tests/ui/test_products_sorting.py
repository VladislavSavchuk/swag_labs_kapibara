"""
Testing the products sorting functionality of saucedemo.com.

This module contains a suite of tests to verify the products sorting
functionality of the saucedemo.com website. Each test checks different
available options for sorting order: ascending by alphabet (default),
descending by alphabet, ascending by price and descending by price.
"""

import logging
import pytest
from pages.login_page import LoginPage
from pages.all_products_page import AllProductsPage
from test_data.login_creds import (STANDARD_USER, STANDARD_PASSWORD)
from test_data import sorting_options_data


@pytest.mark.product_sort
@pytest.mark.smoke
@pytest.mark.uitests
def test_default_sorting(driver):
    """
    Test default product sorting.

    This test verifies that user can see the default sorting on products page.
    The test asserts that:
        default selected sorting option is 'Name (A to Z)',
        sorting dropdown has all necessary options in it,
        products are sorted according to selected option
    """
    logging.info("TC12. Verify that products are sorted by alphabet in "
                 "ascending order by default")

    login_page = LoginPage(driver)
    all_products_page = AllProductsPage(driver)
    login_page.login(STANDARD_USER, STANDARD_PASSWORD)

    assert (sorting_options_data.ABC_ASC
            in all_products_page.get_active_sorting_option_text())
    logging.info("Default product sorting option displayed correctly")

    all_products_page.click_sorting_selector()
    assert (all_products_page.get_all_sorting_options_text() ==
            [sorting_options_data.ABC_ASC,
             sorting_options_data.ABC_DESC,
             sorting_options_data.PRICE_ASC,
             sorting_options_data.PRICE_DESC])
    logging.info("Sorting dropdown displays product sorting options "
                 "correctly")

    assert (all_products_page.get_all_products_titles() ==
            sorted(all_products_page.get_all_products_titles()))
    logging.info("Products are sorted correctly")


@pytest.mark.product_sort
@pytest.mark.smoke
@pytest.mark.uitests
def test_sorting_abc_desc(driver):
    """
    Test product sorting by alphabet in descending order.

    This test verifies that user can change product sorting to "Name (Z to A)"
    The test asserts that products became sorted according to selected option.
    """
    logging.info("TC13. Verify that user can filter products by alphabet in "
                 "descending order")

    login_page = LoginPage(driver)
    all_products_page = AllProductsPage(driver)
    login_page.login(STANDARD_USER, STANDARD_PASSWORD)

    product_titles = all_products_page.get_all_products_titles()
    all_products_page.select_sorting_option(all_products_page.sorting_abc_desc)

    assert (all_products_page.get_all_products_titles() ==
            product_titles[::-1])
    logging.info("Products are sorted correctly")


@pytest.mark.product_sort
@pytest.mark.smoke
@pytest.mark.uitests
def test_sorting_price_asc(driver):
    """
    Test product sorting by price in ascending order.

    This test verifies that user can change product sorting to
    "Price (low to high)"
    The test asserts that products became sorted according to selected option.
    """
    logging.info("TC14. Verify that user can filter products by price in "
                 "ascending order")

    login_page = LoginPage(driver)
    all_products_page = AllProductsPage(driver)
    login_page.login(STANDARD_USER, STANDARD_PASSWORD)

    sorted_product_prices = sorted(all_products_page.get_all_products_prices())
    all_products_page.select_sorting_option(
        all_products_page.sorting_price_asc)

    assert (all_products_page.get_all_products_prices() ==
            sorted_product_prices)
    logging.info("Products are sorted correctly")


@pytest.mark.product_sort
@pytest.mark.smoke
@pytest.mark.uitests
def test_sorting_price_desc(driver):
    """
    Test product sorting by price in descending order.

    This test verifies that user can change product sorting to
    "Price (high to low)"
    The test asserts that products became sorted according to selected option.
    """
    logging.info("TC15. Verify that user can filter products by price in "
                 "descending order")

    login_page = LoginPage(driver)
    all_products_page = AllProductsPage(driver)
    login_page.login(STANDARD_USER, STANDARD_PASSWORD)

    sorted_product_prices = sorted(all_products_page.get_all_products_prices())
    all_products_page.select_sorting_option(
        all_products_page.sorting_price_desc)

    assert (all_products_page.get_all_products_prices() ==
            sorted_product_prices[::-1])
    logging.info("Products are sorted correctly")
