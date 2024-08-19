"""
Testing the products page of saucedemo.com.
This module contains a test to check the 'Add to card' click
"""

import logging
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def test_add_to_cart_button(driver):
    """Step 1: Go to specific product page"""
    product_url = "https://www.saucedemo.com/inventory-item.html?id=5"
    logging.info(f"Navigating to product page: {product_url}")
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
