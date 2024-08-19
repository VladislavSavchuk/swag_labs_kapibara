"""
Testing the products page of saucedemo.com.
This module contains a set of test to check url ID
"""

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# from pages.product_page import ProductItemPage  # надо импортировать?

@pytest.mark.parametrize("product_id, expected_name", [
    (5, "Sauce Labs Fleece Jacket"),  # Existing Product
    (10, "ITEM NOT FOUND"),  # Non-existent product
])
def test_product_page(driver, product_id, expected_name):
    url = f"https://www.saucedemo.com/inventory-item.html?id={product_id}"
    driver.get(url)

    # We expect that the element with the class
    product_name_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME,
                                        "inventory_details_name"))
    )

    # Extracting text from an element
    product_name = product_name_element.text

    # Checking the product name or error message on the page
    print(product_name)  # or logging.info(product_name)

    # Checking the product name or error message on the page
    assert expected_name in product_name, \
        f"Expected '{expected_name}', but got '{product_name}'"
