""" This module contains the BaseAPI class. """

import os
from dotenv import load_dotenv
import requests

load_dotenv()


class BaseAPI:
    """ Base class for API methods. """
    def __init__(self, base_url):
        """ Initializes the BaseAPI with the provided base URL. """
        self.base_url = base_url
        self.key = os.getenv('API-KEY')
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Api Key {self.key}'
        }

    def get(self, endpoint, params=None):
        """ Gets the response from the API. """
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url, params=params,
                                headers=self.headers, timeout=5)
        return response

    def post(self, endpoint, json_data=None):
        """ Posts the response from the API. """
        url = f"{self.base_url}{endpoint}"
        response = requests.post(url, json=json_data, headers=self.headers,
                                 timeout=5)
        return response

    def put(self, endpoint, json_data=None):
        """ Puts the response from the API. """
        url = f"{self.base_url}{endpoint}"
        response = requests.put(url, json=json_data, headers=self.headers,
                                timeout=5)
        return response

    def delete(self, endpoint):
        """ Deletes the response from the API. """
        url = f"{self.base_url}{endpoint}"
        response = requests.delete(url, headers=self.headers, timeout=5)
        return response
