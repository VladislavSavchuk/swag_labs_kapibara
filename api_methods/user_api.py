""" This module contains the UserAPI class. """

import uuid
from api_methods.base_api import BaseAPI
from tests.api.config import BASE_URL


def generate_random_username():
    """Generate random username using UUID."""
    unique_id = uuid.uuid4()
    random_username = f"user_{unique_id}"
    return random_username


class UserAPI(BaseAPI):
    """ User API class. """
    def __init__(self):
        """ Initializes the UserAPI. """
        super().__init__(BASE_URL)

    def create_user(self, user_data):
        """ Creates a new user. """
        return self.post("/user", user_data)

    def get_user(self, username):
        """ Gets a user. """
        return self.get(f"/user/{username}")

    def update_user(self, username, user_data):
        """ Updates a user. """
        return self.put(f"/user/{username}", user_data)

    def delete_user(self, username):
        """ Deletes a user. """
        return self.delete(f"/user/{username}")
