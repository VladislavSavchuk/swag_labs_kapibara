"""
Testing the products page of saucedemo.com.
This module contains a set of test to check url ID
"""

import logging
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.url import BASE_URL, TEST_PRODUCTS


@pytest.mark.parametrize("product_id, expected_name", TEST_PRODUCTS)
def test_product_page(driver, product_id, expected_name):
    url = f"{BASE_URL}{product_id}"
    driver.get(url)

    try:
        # Waiting for an element with a class
        product_name_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME,
                                            "inventory_details_name"))
        )
        product_name = product_name_element.text
    except Exception as e:
        # Handling exceptions if element not found
        product_name = str(e)
        logging.error(f"Error finding element: {product_name}")

    # Checking the product name or error message on the page
    logging.info(f"Product name on page: {product_name}")

    # Checking the product name or error message on the page
    assert expected_name in product_name, \
        f"Expected '{expected_name}', but got '{product_name}'"
