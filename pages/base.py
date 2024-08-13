"""
This module contains the BasePage class which provides common
functionalities for interacting with web pages using Selenium WebDriver.
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """
    A base page class that encapsulates common functionalities
    for interacting with web pages using Selenium WebDriver.
    """
    def __init__(self, driver):
        """
        Initializes the BasePage with the provided WebDriver
        instance and sets up the WebDriverWait.

        Parameters:
            driver (selenium.webdriver.remote.webdriver.WebDriver):
                The WebDriver instance used to interact with the browser.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator):
        """
        Finds an element on the page using the provided locator.

        Parameters:
            locator (tuple):
                A tuple containing the method to locate the element
                and the locator value (e.g., (By.CSS_SELECTOR, 'selector')).

        Returns:
            selenium.webdriver.remote.webelement.WebElement:
                The located element.

        Raises:
            TimeoutException:
                If the element is not found within the timeout period.
        """
        return self.wait.until(EC.presence_of_element_located(locator))

    def click_element(self, locator):
        """
        Clicks on an element located by the provided locator.

        Parameters:
            locator (tuple):
                A tuple containing the method to locate the element
                and the locator value (e.g., (By.CSS_SELECTOR, 'selector')).

        Raises:
            TimeoutException:
                If the element is not clickable within the timeout period.
        """
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def enter_text(self, locator, text):
        """
        Enters text into an input field located by the provided locator.

        Parameters:
            locator (tuple):
                A tuple containing the method to locate the element
                and the locator value (e.g., (By.CSS_SELECTOR, 'selector')).
            text (str):
                The text to enter into the input field.

        Raises:
            TimeoutException:
                If the element is not found or the input field is not
                interactable within the timeout period.

        Returns:
            bool:
                True if the text was successfully entered, False otherwise.
        """
        element = self.find_element(locator)
        if element:
            element.clear()
            element.send_keys(text)
            return True
        return False

    def get_text(self, locator):
        """
        Gets element text by the provided locator.

        Parameters:
            locator (tuple):
                A tuple containing the method to locate the element
                and the locator value (e.g., (By.CSS_SELECTOR, 'selector')).

        Raises:
            TimeoutException:
                If the element is not clickable within the timeout period.
        """
        return self.wait.until(
            EC.visibility_of_element_located(locator)).text

    def get_all_elements_texts(self, locator):
        """
        Gets all elements texts by the provided locator.

        Parameters:
            locator (tuple):
                A tuple containing the method to locate the element
                and the locator value (e.g., (By.CSS_SELECTOR, 'selector')).

        Raises:
            TimeoutException:
                If the element is not clickable within the timeout period.
        """
        elements = self.wait.until(
            EC.visibility_of_all_elements_located(locator))

        texts = []
        for elem in elements:
            text = elem.text
            texts.append(text)
        return texts
