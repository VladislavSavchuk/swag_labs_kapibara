"""Login page locators"""

from selenium.webdriver.common.by import By


class LoginPageLocators:
    """The class contains locators to login page """
    # logo
    login_logo = (By.CLASS_NAME, "login_logo")

    # form
    login_form = (By.XPATH,
                  '//*[@id="login_button_container"]/div/form')
    input_username = (By.ID, "user-name")
    input_password = (By.ID, "password")

    # buttons
    login_btn = (By.ID, "login-button")

    # messages
    error_msg = (By.CSS_SELECTOR,
                 "#login_button_container > div > form > div.error-message-container.error")
