"""Module for storing schemes for Petstore testing"""

get_put_pet = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "photoUrls": {"type": "array", "items": {"type": "string"}},
        "status": {"type": "string", "enum": ["available", "pending", "sold"]}
    },
    "required": ["id", "status"]
}

delete_pet = {
    "type": "object",
    "properties": {
        "code": {"type": "integer"},
        "type": {"type": "string"},
        "message": {"type": "string"}
    },
    "required": ["code", "message"]
}
