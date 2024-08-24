""" This module contains the UserAPI class. """

import logging
import pytest
from jsonschema import validate, ValidationError
from api_methods.user_api import UserAPI
from test_data.api.user_data import (
    user_data, updated_user_data, login_user_payload,
    login_user_negative_payload)
from test_data.api.user_schemes import \
    post_put_delete_user_schema, get_user_schema


@pytest.fixture(scope="module")
def user_api():
    """Fixture to initialize UserAPI."""
    return UserAPI()


@pytest.fixture
def random_user_data():
    """Fixture to generate random user data."""
    return user_data


@pytest.mark.api
@pytest.mark.user_api
@pytest.mark.smoke
def test_create_user(user_api, random_user_data):
    """Creates a new user and returns its username."""
    logging.info("API-TC01. Verify ability to create a new user")

    response = user_api.create_user(random_user_data)
    response_data = response.json()

    logging.info(f"Response status code: {response.status_code}")
    logging.info(f"Response data: {response}")

    try:
        validate(instance=response_data,
                 schema=post_put_delete_user_schema)
    except ValidationError as e:
        pytest.fail(f"Response JSON does not match schema: {e.message}")

    assert response.status_code == 200, \
        f'Expected 200, got {response.status_code}'

    assert response_data['code'] == 200, 'Unexpected response code'

    logging.info("User created successfully, response schema is correct")


@pytest.mark.api
@pytest.mark.user_api
@pytest.mark.smoke
def test_get_user(user_api, random_user_data):
    """ This test verifies that a user is retrieved by username. """
    logging.info("API-TC02. Verify ability to get user info by username")

    user_api.create_user(random_user_data)
    response = user_api.get_user(random_user_data['username'])
    response_data = response.json()

    logging.info(f"Response status code: {response.status_code}")
    logging.info(f"Response data: {response_data}")

    try:
        validate(instance=response_data, schema=get_user_schema)
    except ValidationError as e:
        pytest.fail(f"Response JSON does not match schema: {e.message}")

    assert response.status_code == 200, \
        f'Expected 200, got {response.status_code}'

    assert response_data['username'] == random_user_data['username'], \
        "Username does not match"

    logging.info("User retrieved successfully, response schema is correct")


@pytest.mark.api
@pytest.mark.user_api
@pytest.mark.smoke
def test_update_user(user_api, random_user_data):
    """ This test verifies that a user is updated by username. """
    logging.info("API-TC03. Verify ability to update user by username")

    user_api.create_user(random_user_data)
    updated_data = updated_user_data.copy()

    response = user_api.update_user(random_user_data['username'],
                                    updated_data)
    response_data = response.json()

    logging.info(f"Response status code: {response.status_code}")
    logging.info(f"Response data: {response_data}")

    try:
        validate(instance=response_data,
                 schema=post_put_delete_user_schema)
    except ValidationError as e:
        pytest.fail(f"Response JSON does not match schema: {e.message}")

    assert response.status_code == 200, \
        f'Expected 200, got {response.status_code}'

    assert response_data['code'] == 200, 'Unexpected response code'

    logging.info("User updated successfully, response schema is correct")


@pytest.mark.api
@pytest.mark.user_api
@pytest.mark.smoke
def test_delete_user(user_api, random_user_data):
    """ This test verifies that a user is deleted by username. """
    logging.info("API-TC04. Verify ability to delete user by username")

    user_api.create_user(random_user_data)
    response = user_api.delete_user(random_user_data['username'])
    response_data = response.json()

    logging.info(f"Response status code: {response.status_code}")
    logging.info(f"Response data: {response_data}")

    try:
        validate(instance=response_data,
                 schema=post_put_delete_user_schema)
    except ValidationError as e:
        pytest.fail(f"Response JSON does not match schema: {e.message}")

    assert response.status_code == 200, \
        f'Expected 200, got {response.status_code}'

    assert response_data['code'] == 200, 'Unexpected response code'

    logging.info("User deleted successfully, response schema is correct")


@pytest.mark.api
@pytest.mark.user_api
@pytest.mark.smoke
def test_user_login(user_api, random_user_data):
    """ This test verifies that a user is login """
    logging.info("API-TC05. Verify ability to login")

    user_api.create_user(random_user_data)
    login_payload = login_user_payload.copy()
    response = user_api.user_login(login_payload)
    response_data = response.json()

    logging.info(f"Response status code: {response.status_code}")
    logging.info(f"Response data: {response_data}")

    assert response.status_code == 200, \
        f'Expected 200, got {response.status_code}'

    assert response_data['code'] == 200, 'Unexpected response code'

    logging.info("User logged in successfully")


@pytest.mark.api
@pytest.mark.user_api
@pytest.mark.smoke
def test_user_logout(user_api):
    """ This test verifies that a user is logout """
    logging.info("API-TC06. Verify ability to logout")

    response = user_api.user_logout()
    response_data = response.json()

    logging.info(f"Response status code: {response.status_code}")
    logging.info(f"Response data: {response_data}")

    assert response.status_code == 200, \
        f'Expected 200, got {response.status_code}'

    assert response_data['code'] == 200, 'Unexpected response code'

    logging.info("User logged out successfully")


@pytest.mark.api
@pytest.mark.user_api
@pytest.mark.smoke
@pytest.mark.xfail(reason="Expected 400 error code, but got 200")
def test_user_login_negative(user_api):
    """ This test verifies negative login """
    logging.info("API-TC07. Verify inability to login "
                 "with non-existing user")

    login_payload = login_user_negative_payload.copy()
    response = user_api.user_login(login_payload)
    response_data = response.json()

    logging.info(f"Response status code: {response.status_code}")
    logging.info(f"Response data: {response_data}")

    assert response.status_code == 400, \
        f'Expected 400, got {response.status_code}'

    assert response_data['code'] == 400, 'Unexpected response code'

    logging.info("User login failed")
