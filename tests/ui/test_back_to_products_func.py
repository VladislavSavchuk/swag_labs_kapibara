"""
Testing the products page of saucedemo.com.
This module contains a test to check the 'Back to products' click
"""

import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def test_back_to_products_button(driver):
    """Step 1: Go to specific product page"""
    product_url = "https://www.saucedemo.com/inventory-item.html?id=5"
    logging.info(f"Navigating to product page: {product_url}")
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
