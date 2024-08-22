"""Module for storing schemes for /store/order testing"""

get_order = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "petId": {"type": "integer"},
        "quantity": {"type": "integer"},
        "shipDate": {"type": "string"},
        "status": {"type": "string"},
        "complete": {"type": "boolean"}
    },
    "required": ["id", "petId", "quantity", "status", "complete"]
}

delete_order = {
    "type": "object",
    "properties": {
        "code": {"type": "integer"},
        "type": {"type": "string"},
        "message": {"type": "string"}
    },
    "required": ["code", "message"]
}
