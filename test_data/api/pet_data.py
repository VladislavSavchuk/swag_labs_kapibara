"""This method contains data for /pet requests"""

# Pet
create_pet_valid = {
    "name": "Shket",
    "status": "available"
    }


def update_pet_valid(pet_id):
    """Return data for pet updating"""
    return {
        "id": pet_id,
        "status": "sold"}


update_pet_invalid = {
    "id": "",
    "status": "sold"
}
