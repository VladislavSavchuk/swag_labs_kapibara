"""
Testing the login page of saucedemo.com.

This module contains a suite of tests to verify the login functionality
of the saucedemo.com website. Each test checks different scenarios
of logging in with various user credentials, including valid, invalid,
empty, and locked-out user cases.
"""

import logging
import pytest
from pages.login_page import LoginPage
from test_data.login_creds import (
    STANDARD_USER, LOCKED_OUT_USER, EMPTY_STRING, STANDARD_PASSWORD)


@pytest.mark.login
@pytest.mark.smoke
@pytest.mark.uitests
@pytest.mark.login_success
def test_login_valid_user(driver):
    """
    Test logging in with a valid username and password.

    This test verifies that a user can successfully log in with
    correct credentials. The test asserts that no error message
    appears on the page after the login attempt.
    """
    logging.info("Verifying that user can login with correct creds")

    login_page = LoginPage(driver)
    login_page.login(username=STANDARD_USER, password=STANDARD_PASSWORD)

    assert not login_page.error_message_exists()
    logging.info("Successfully verified user login with correct creds")


@pytest.mark.login
@pytest.mark.uitests
@pytest.mark.login_incorrect
def test_login_invalid_user(driver):
    """
    Test logging in with an invalid username and password.

    This test verifies that logging in with incorrect credentials
    results in an error message being displayed on the page.
    """
    logging.info("Verifying that user cannot login with incorrect creds")

    login_page = LoginPage(driver)
    login_page.login(
        username="non_existent_user", password="wrong_password123")

    assert login_page.error_message_exists()
    logging.info("Successfully verified user login with incorrect creds")


@pytest.mark.login
@pytest.mark.uitests
@pytest.mark.login_incorrect
def test_login_empty_blank(driver):
    """
    Test logging in with an empty username and password.

    This test verifies that an error message is displayed when the user
    attempts to log in without entering a username or password.
    """
    logging.info(
        "Verifying that user cannot login with empty username and password")

    login_page = LoginPage(driver)
    login_page.login(username=EMPTY_STRING, password=EMPTY_STRING)

    assert login_page.error_message_exists()
    logging.info(
        "Successfully verified user login with empty username and password")


@pytest.mark.login
@pytest.mark.uitests
@pytest.mark.login_incorrect
def test_login_locked_out_user(driver):
    """
    Test logging in with a locked-out user.

    This test verifies that attempting to log in with a locked-out user's
    credentials results in an error message being displayed on the page.
    """
    logging.info("Verifying that user cannot login with locked out user")

    login_page = LoginPage(driver)
    login_page.login(username=LOCKED_OUT_USER, password=STANDARD_PASSWORD)

    assert login_page.error_message_exists()
    logging.info("Successfully verified user login with locked out user")
