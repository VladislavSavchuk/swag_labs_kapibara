"""
Testing the products page of saucedemo.com.
This module contains a set of test to check url ID
"""

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
        # Ожидание элемента с классом
        product_name_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME,
                                            "inventory_details_name"))
        )
        product_name = product_name_element.text
    except Exception as e:
        # Обработка исключений, если элемент не найден
        product_name = str(e)

    # Проверка названия продукта или сообщения об ошибке на странице
    print(product_name)  # или logging.info(product_name)

    # Проверка названия продукта или сообщения об ошибке на странице
    assert expected_name in product_name, \
        f"Expected '{expected_name}', but got '{product_name}'"
