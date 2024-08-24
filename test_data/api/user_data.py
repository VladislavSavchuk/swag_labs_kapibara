""" This module contains data for /user requests """

import random
from api_methods.user_api import generate_random_username

random_username = generate_random_username()

user_data = {
    "id": random.randint(1, 1000),
    "username": random_username,
    "firstName": "John",
    "lastName": "Doe",
    "email": "johndoe@example.com",
    "password": "password123",
    "phone": "+123456789",
    "userStatus": 0
}

updated_user_data = {
    "firstName": "Mary",
    "lastName": "Smith",
    "email": "marysmith@example.com",
    "phone": "+987654321",
    "userStatus": 1
}

login_user_payload = {
        "username": "test",
        "password": "abc123"
    }

login_user_negative_payload = {
        "username": "test_negative",
        "password": "abc1234"
    }

