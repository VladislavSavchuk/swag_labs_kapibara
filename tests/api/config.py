# config.py

BASE_URL = "https://petstore.swagger.io/v2"

user_schema_1 = {
    "type": "object",
    "properties": {
        "code": {"type": "integer"},
        "type": {"type": "string"},
        "message": {"type": "string"}
    },
    "required": ["code", "type", "message"]
}

user_schema_2 = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "username": {"type": "string"},
        "firstName": {"type": "string"},
        "lastName": {"type": "string"},
        "email": {"type": "string"},
        "password": {"type": "string"},
        "phone": {"type": "string"},
        "userStatus": {"type": "integer"},
    },
    "required": ["id", "username", "firstName", "lastName",
                 "email", "password", "phone", "userStatus"]
}
