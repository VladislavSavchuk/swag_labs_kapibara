""" This module contains the BaseAPI class. """

import requests


class BaseAPI:
    """ Base class for API methods. """
    def __init__(self, base_url):
        """ Initializes the BaseAPI with the provided base URL. """
        self.base_url = base_url

    def get(self, endpoint, params=None, headers=None):
        """ Gets the response from the API. """
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url, params=params, headers=headers)
        return response

    def post(self, endpoint, data=None, json=None, headers=None):
        """ Posts the response from the API. """
        url = f"{self.base_url}{endpoint}"
        response = requests.post(url, data=data, json=json, headers=headers)
        return response

    def put(self, endpoint, data=None, json=None, headers=None):
        """ Puts the response from the API. """
        url = f"{self.base_url}{endpoint}"
        response = requests.put(url, data=data, json=json, headers=headers)
        return response

    def delete(self, endpoint, headers=None):
        """ Deletes the response from the API. """
        url = f"{self.base_url}{endpoint}"
        response = requests.delete(url, headers=headers)
        return response
