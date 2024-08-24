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
    logging.info("API-TC08. Verify ability to add a new pet to the store")
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
    logging.info("API-TC09. Verify ability to get pet info by its ID")
    pet = Pet()

    pet_id = str(pet.add_pet(pet_data.create_pet_valid).json()["id"])
    logging.info("New pet created")

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
    logging.info("API-TC10. Verify ability to update pet")
    pet = Pet()

    pet_id = str(pet.add_pet(pet_data.create_pet_valid).json()["id"])
    logging.info("New pet created")

    update_pet_response = pet.update_pet(
        pet_data.update_pet_valid(pet_id))

    assert update_pet_response.status_code == 200
    assert (validate(update_pet_response.json(), pet_schemes.get_put_pet)
            is not ValidationError)
    assert (update_pet_response.json()["status"] ==
            pet_data.update_pet_valid(pet_id)["status"])
    logging.info("Pet updated successfully, response schema is correct")

    logging.info("Delete created pet")
    delete = pet.delete_pet(pet.pet_id)
    assert delete.status_code == 200
    logging.info("Pet deleted")


@pytest.mark.api
@pytest.mark.pet_api
@pytest.mark.smoke
def test_delete_pet():
    """Test deleting a pet"""
    logging.info("API-TC11. Verify ability to delete pet")
    pet = Pet()

    pet.add_pet(pet_data.create_pet_valid)
    logging.info("New pet created")

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
    logging.info("API-TC12. Verify inability to delete an already deleted pet")
    pet = Pet()

    pet.add_pet(pet_data.create_pet_valid).json()
    logging.info("New pet created")

    pet.delete_pet(pet.pet_id)
    logging.info("Pet deleted")
    delete_pet_response = pet.delete_pet(pet.pet_id)
    logging.info("Try to delete already deleted pet")

    assert delete_pet_response.status_code == 404
    logging.info("DELETE Request sent successfully, error code "
                 f"{delete_pet_response.status_code} is correct")


@pytest.mark.api
@pytest.mark.pet_api
@pytest.mark.smoke
@pytest.mark.xfail(reason="Expected 400 error code, but got 200")
def test_update_pet_negative():
    """Test updating a created pet using empty id in request body"""
    logging.info("API-TC13. Verify inability to update pet with empty ID")
    pet = Pet()

    update_pet_neg_response = pet.update_pet(pet_data.update_pet_invalid)

    assert (update_pet_neg_response.status_code ==
            400), AssertionError("Unexpected status code")
    logging.info("PUT Request sent successfully, error code is correct")
