""" This module contains the Order class. """

from api_methods.base_api import BaseAPI
from tests.api.config import BASE_URL


class Order(BaseAPI):
    """ Order API class. """
    def __init__(self):
        """ Initializes the Order class """
        super().__init__(BASE_URL)
        self.endpoint = "/store/order/"
        self.order_id = ""

    def create_order(self, create_order):
        """ Place a new order for a pet """
        response = self.post(self.endpoint, create_order)
        self.order_id = str(response.json()["id"])
        return response

    def get_order(self, order_id):
        """ Find purchase order by ID """
        return self.get(self.endpoint + order_id)

    def delete_order(self, order_id):
        """ Delete purchase order by ID """
        return self.delete(self.endpoint + order_id)
