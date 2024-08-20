""" This module contains the UserAPI class. """

import logging
import pytest
from api_methods.user_api import UserAPI, generate_random_username


@pytest.fixture(scope="module")
def user_api():
    """ Initializes the UserAPI. """
    return UserAPI()


@pytest.fixture(scope="module")
def created_user(user_api):
    """Creates a new user and returns its username."""
    random_username = generate_random_username()
    user_data = {
        "id": 0,
        "username": random_username,
        "firstName": "John",
        "lastName": "Wick",
        "email": "johnwick@example.com",
        "password": "qwerty",
        "phone": "1234567890",
        "userStatus": 1
    }
    response = user_api.create_user(user_data)
    response_data = response.json()
    logging.info(f"Response status code: {response.status_code}")
    logging.info(f"Response data: {response_data}")

    assert response.status_code == 200, \
        f'Expected 200, got {response.status_code}'
    assert response_data['code'] == 200, 'Unexpected response code'

    return random_username


@pytest.mark.api
@pytest.mark.smoke
def test_get_user(user_api, created_user):
    """ This test verifies that a user is retrieved by username. """
    logging.info("Test Get user by username")

    response = user_api.get_user(created_user)
    response_data = response.json()
    logging.info(f"Response status code: {response.status_code}")
    logging.info(f"Response data: {response_data}")

    assert response.status_code == 200, \
        f'Expected 200, got {response.status_code}'
    assert response_data["username"] == created_user

    logging.info("Successfully retrieved user")


@pytest.mark.api
@pytest.mark.smoke
def test_update_user(user_api, created_user):
    """ This test verifies that a user is updated by username. """
    logging.info("Test Update user by username")

    random_username = generate_random_username()

    updated_user_data = {
        "id": 0,
        "username": random_username,
        "firstName": "John",
        "lastName": "Smith",
        "email": "johnsmith@example.com",
        "password": "qwerty123",
        "phone": "0987654321",
        "userStatus": 1
    }

    response = user_api.update_user(created_user, updated_user_data)
    response_data = response.json()
    logging.info(f"Response status code: {response.status_code}")
    logging.info(f"Response data: {response_data}")

    assert response.status_code == 200, \
        f'Expected 200, got {response.status_code}'
    assert response_data['code'] == 200, 'Unexpected response code'

    logging.info("Successfully updated user")

    return random_username


@pytest.mark.api
@pytest.mark.smoke
def test_delete_user(user_api, created_user):
    """ This test verifies that a user is deleted by username. """
    logging.info("Test Delete user by username")

    updated_user_data = test_update_user(user_api, created_user)

    response = user_api.delete_user(updated_user_data)
    response_data = response.json()
    logging.info(f"Response status code: {response.status_code}")
    logging.info(f"Response data: {response_data}")

    assert response.status_code == 200, \
        f'Expected 200, got {response.status_code}'
    assert response_data['code'] == 200, 'Unexpected response code'
    assert response_data['message'] == updated_user_data, \
        'Unexpected username'

    logging.info("Successfully deleted user")
