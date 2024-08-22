""" This module contains tests for store/order/ endpoint """

import logging
import pytest
from jsonschema import validate, ValidationError
from api_methods.order_api import Order
from test_data.api import order_data
from test_data.api import order_schemes


@pytest.mark.api
@pytest.mark.order_api
@pytest.mark.smoke
def test_place_order():
    """Test creating a new order"""
    logging.info("Test POST request to /store/order endpoint and verify that "
                 "new order places to the store")
    order = Order()

    response = order.create_order(order_data.create_order)
    assert response.status_code == 200
    logging.info("POST Request sent successfully")

    logging.info("Delete placed order")
    delete = order.delete_order(order.order_id)
    logging.info(delete)
    assert delete.status_code == 200
    logging.info("Order deleted")


@pytest.mark.api
@pytest.mark.order_api
@pytest.mark.smoke
def test_get_order():
    """Test getting a created order"""
    logging.info("Test GET request to store/order/{order_id} endpoint and "
                 "verify that new order added to the store")
    order = Order()

    order_id = str(order.create_order(order_data.create_order).json()["id"])
    logging.info("New order created")

    get_order_response = order.get_order(order_id)

    assert get_order_response.status_code == 200
    assert (validate(get_order_response.json(), order_schemes.get_order)
            is not ValidationError)
    assert (get_order_response.json()["petId"] ==
            order_data.create_order["petId"])
    logging.info("GET Request sent successfully, response schema is correct")

    logging.info("Delete created order")
    delete_order_response = order.delete_order(order.order_id)
    assert delete_order_response.status_code == 200
    logging.info("Order deleted")


@pytest.mark.api
@pytest.mark.order_api
@pytest.mark.smoke
def test_delete_order():
    """Test deleting an order"""
    logging.info("Test DELETE request to store/order/{order_id} endpoint and "
                 "verify that order deleted")
    order = Order()

    order.create_order(order_data.create_order)
    logging.info("New order created")

    delete_order_response = order.delete_order(order.order_id)

    assert delete_order_response.status_code == 200
    assert (validate(delete_order_response.json(), order_schemes.delete_order)
            is not ValidationError)
    assert delete_order_response.json()["message"] == order.order_id
    logging.info("DELETE Request sent successfully, response schema is "
                 "correct")


@pytest.mark.api
@pytest.mark.order_api
@pytest.mark.smoke
def test_delete_order_negative():
    """Test deleting an already deleted order"""
    logging.info("Test DELETE request to store/order/{order_id} endpoint twice"
                 " and verify error code")
    order = Order()

    order.create_order(order_data.create_order).json()
    logging.info("New order created")

    order.delete_order(order.order_id)
    logging.info("Delete a order")
    delete_order_response = order.delete_order(order.order_id)
    logging.info("Try to delete already deleted order")

    assert delete_order_response.status_code == 404
    logging.info("DELETE Request sent successfully, error code "
                 f"{delete_order_response.status_code} is correct")


@pytest.mark.api
@pytest.mark.order_api
@pytest.mark.smoke
def test_get_order_negative():
    """Test updating a created order using id of non existing order in request
        body"""
    logging.info("Test GET request to store/order endpoint with non existing "
                 "order_id in request body and verify response code")
    order = Order()

    get_order_neg_response = order.get_order(order_data.invalid_order_id)

    assert (get_order_neg_response.status_code ==
            404), AssertionError("Unexpected status code")
    logging.info("GET Request sent successfully, error code "
                 f"{get_order_neg_response.status_code} is correct")
