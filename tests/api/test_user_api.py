""" This module contains the UserAPI class. """

import pytest
from api_methods.user_api import UserAPI, generate_random_username


@pytest.fixture(scope="module")
def user_api():
    return UserAPI()


@pytest.mark.api
@pytest.mark.smoke
def test_create_user(user_api):
    """Test creating a new user."""
    random_username = generate_random_username()
    user_data = {
        "id": 0,
        "username": random_username,
        "firstName": "Test",
        "lastName": "User",
        "email": "testuser@example.com",
        "password": "password",
        "phone": "1234567890",
        "userStatus": 1
    }
    response = user_api.create_user(user_data)
    assert response.status_code == 200


# def test_get_user(user_api):
#     response = user_api.get_user("testuser")
#     assert response.status_code == 200
#     assert response.json()["username"] == "testuser"
#
#
# def test_update_user(user_api):
#     updated_user_data = {
#         "id": 0,
#         "username": "testuser",
#         "firstName": "Updated",
#         "lastName": "User",
#         "email": "updateduser@example.com",
#         "password": "newpassword",
#         "phone": "0987654321",
#         "userStatus": 1
#     }
#     response = user_api.update_user("testuser", updated_user_data)
#     assert response.status_code == 200
#
#     # Verify update
#     response = user_api.get_user("testuser")
#     assert response.status_code == 200
#     assert response.json()["firstName"] == "Updated"
#
#
# def test_delete_user(user_api):
#     response = user_api.delete_user("testuser")
#     assert response.status_code == 200
#
#     # Verify deletion
#     response = user_api.get_user("testuser")
#     assert response.status_code == 404
