""" Module for storing schemes for User API testing """

post_put_delete_user_schema = {
    "type": "object",
    "properties": {
        "code": {"type": "integer"},
        "type": {"type": "string"},
        "message": {"type": "string"}
    },
    "required": ["code", "type", "message"]
}


get_user_schema = {
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
