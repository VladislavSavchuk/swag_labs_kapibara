""" This module contains tests for Petstore /pet/ endpoint """

import logging
import pytest
from jsonschema import validate, ValidationError
from api_methods.pet_api import Pet
from test_data.api import pet_data
from test_data.api import pet_schemes


@pytest.mark.api
@pytest.mark.pet_api
@pytest.mark.smoke
def test_add_pet():
    """Test creating a new pet"""
    logging.info("Test POST request to /pet endpoint and verify that new "
                 "pet added to the store")
    pet = Pet()

    response = pet.add_pet(pet_data.create_pet_valid)
    assert response.status_code == 200
    logging.info("POST Request sent successfully")

    logging.info("Delete created pet")
    delete = pet.delete_pet(pet.pet_id)
    assert delete.status_code == 200
    logging.info("Pet deleted")


@pytest.mark.api
@pytest.mark.pet_api
@pytest.mark.smoke
def test_get_pet():
    """Test getting a created pet"""
    logging.info("Test GET request to /pet/{pet_id} endpoint and verify that "
                 "new pet added to the store")
    pet = Pet()

    pet_id = str(pet.add_pet(pet_data.create_pet_valid).json()["id"])
    logging.info("Create a new pet")

    get_pet_response = pet.get_pet(pet_id)

    assert get_pet_response.status_code == 200
    assert (validate(get_pet_response.json(), pet_schemes.get_put_pet)
            is not ValidationError)
    assert get_pet_response.json()["name"] == pet_data.create_pet_valid["name"]
    logging.info("GET Request sent successfully, response schema is correct")

    logging.info("Delete created pet")
    delete_pet_response = pet.delete_pet(pet.pet_id)
    assert delete_pet_response.status_code == 200
    logging.info("Pet deleted")


@pytest.mark.api
@pytest.mark.pet_api
@pytest.mark.smoke
def test_update_pet():
    """Test updating a created pet"""
    logging.info("Test PUT request to /pet endpoint and verify that "
                 "pet updated")
    pet = Pet()

    pet_id = str(pet.add_pet(pet_data.create_pet_valid).json()["id"])
    logging.info("Create a new pet")

    update_pet_response = pet.update_pet(
        pet_data.update_pet_valid(pet_id))

    assert update_pet_response.status_code == 200
    assert (validate(update_pet_response.json(), pet_schemes.get_put_pet)
            is not ValidationError)
    assert (update_pet_response.json()["status"] ==
            pet_data.update_pet_valid(pet_id)["status"])
    logging.info("PUT Request sent successfully, response schema is correct")

    logging.info("Delete created pet")
    delete = pet.delete_pet(pet.pet_id)
    assert delete.status_code == 200
    logging.info("Pet deleted")


@pytest.mark.api
@pytest.mark.pet_api
@pytest.mark.smoke
def test_delete_pet():
    """Test deleting a pet"""
    logging.info("Test DELETE request to /pet/{pet_id} endpoint and verify "
                 "that pet deleted")
    pet = Pet()

    pet.add_pet(pet_data.create_pet_valid)
    logging.info("Create a new pet")

    delete_pet_response = pet.delete_pet(pet.pet_id)

    assert delete_pet_response.status_code == 200
    assert (validate(delete_pet_response.json(), pet_schemes.delete_pet)
            is not ValidationError)
    assert delete_pet_response.json()["message"] == pet.pet_id
    logging.info("DELETE Request sent successfully, response schema is "
                 "correct")


@pytest.mark.api
@pytest.mark.pet_api
@pytest.mark.smoke
def test_delete_pet_negative():
    """Test deleting a deleted pet"""
    logging.info("Test DELETE request to /pet/{pet_id} endpoint twice and "
                 "verify error code")
    pet = Pet()

    pet.add_pet(pet_data.create_pet_valid).json()
    logging.info("Create a new pet")

    pet.delete_pet(pet.pet_id)
    logging.info("Delete a pet")
    delete_pet_response = pet.delete_pet(pet.pet_id)
    logging.info("Try to delete already deleted pet")

    assert delete_pet_response.status_code == 404
    logging.info("DELETE Request sent successfully, error code "
                 f"{delete_pet_response.status_code} is correct")


@pytest.mark.api
@pytest.mark.pet_api
@pytest.mark.smoke
def test_update_pet_negative():
    """Test updating a created pet using empty id in request body"""
    logging.info("Test PUT request to /pet endpoint with empty id in request "
                 "body and verify response code")
    pet = Pet()

    update_pet_neg_response = pet.update_pet(pet_data.update_pet_invalid)

    assert (update_pet_neg_response.status_code ==
            400), AssertionError("Unexpected status code")
    logging.info("PUT Request sent successfully, error code is correct")
