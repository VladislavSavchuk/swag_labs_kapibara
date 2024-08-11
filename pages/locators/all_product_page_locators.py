"""Product page locators"""

from selenium.webdriver.common.by import By


class ProductPageLocators:
    """The class contains locators to product page """
    app_logo = (By.CLASS_NAME, "app_logo")
    burger_menu = (By.ID, "react-burger-menu-btn")
    shopping_cart_icon = (By.ID, "shopping_cart_container")
    product_sort = '[data-test="active-option"]'

    # buttons
    add_to_cart_backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
    add_to_cart_light = (By.ID, "add-to-cart-sauce-labs-bike-light")
    add_to_cart_shirt = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    add_to_cart_jacket = (By.ID, "add-to-cart-sauce-labs-fleece-jacket")
    add_to_cart_onesie = (By.ID, "add-to-cart-sauce-labs-onesie")
    add_to_cart_shirt_red = (
        By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)")
