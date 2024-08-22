"""base_url"""

BASE_URL = "https://www.saucedemo.com/inventory-item.html?id="

# Test data: list of tuples (product_id, expected_name)
TEST_PRODUCTS = [
    (5, "Sauce Labs Fleece Jacket"),  # Существующий продукт
    (10, "ITEM NOT FOUND"),  # Несуществующий продукт
]
