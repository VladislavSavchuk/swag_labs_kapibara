""" This module contains the Pet class. """

from api_methods.base_api import BaseAPI
from tests.api.config import BASE_URL


class Pet(BaseAPI):
    """ Pet API class. """
    def __init__(self):
        """ Initializes the Pet class """
        super().__init__(BASE_URL)
        self.endpoint = "/pet/"
        self.pet_id = ""

    def add_pet(self, create_pet):
        """ Add a new pet to the store """
        response = self.post(self.endpoint, create_pet)
        self.pet_id = str(response.json()["id"])
        return response

    def get_pet(self, pet_id):
        """ Find pet by ID """
        return self.get(self.endpoint + pet_id)

    def update_pet(self, update_pet):
        """ Update an existing pet """
        return self.put(self.endpoint, update_pet)

    def delete_pet(self, pet_id):
        """ Deletes a pet """
        return self.delete(self.endpoint + pet_id)
