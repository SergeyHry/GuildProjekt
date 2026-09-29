// POST /api/auth/login
REQUEST
{
    "type": "object",
    "properties": {
    "email": {
        "type": "string",
            "format": "email",
    },
    "password": {
        "type": "string",
        "minLength": 8,
        "maxLength": 30
    }
},
    "required": ["email", "password"]
}
RESPONSE
{
    "type": "object",
    "properties": {
    "access_token": {
        "type": "string",
    },
    "token_type": {
        "type": "string",
    },
    "expires_in": {
        "type": "integer",
            "example": 3600,
            "description": "Gültigkeit des Tokens in Sekunden"
    },
    "user": {
        "type": "object",
            "properties": {
            "id": {
                "type": "int",
            },
            "username": {
                "type": "string"
            },
            "email": {
                "type": "string",
            }
        },
        "required": ["id", "username", "email"]
    }
},
    "required": ["access_token", "token_type", "user"]
}
POST /api/auth/registration
REQUEST
{
    "type": "object",
    "properties": {
        "firstname": {
            "type": "string",
            "minLength": 2,
            "maxLength": 50
        },
        "lastname": {
            "type": "string",
            "minLength": 2,
            "maxLength": 50
        },
        "username": {
            "type": "string",
            "minLength": 3,
            "maxLength": 30
        },
        "email": {
            "type": "string",
            "format": "email"
        },
        "password": {
            "type": "string",
            "minLength": 8
        },
        "inviteCode": {
            "type": "string"
        }
    },
    "required": [
        "firstname",
        "lastname",
        "username",
        "email",
        "password",
        "inviteCode"
    ]
}
RESPONSE
{
    "type": "object",
    "properties": {
        "id": {
            "type": "string",
            "format": "uuid"
        },
        "firstname": {
            "type": "string"
        },
        "lastname": {
            "type": "string"
        },
        "username": {
            "type": "string"
        },
        "email": {
            "type": "string",
            "format": "email"
        }
    },
    "required": [
        "id",
        "firstname",
        "lastname",
        "username",
        "email"
    ]
}
//GET /api/users
REQUEST
{}
RESPONSE
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "id":{"int"},
      "nickname": { "type": "string"}
    }
  }
}
//GET /api/users/{id}
REQUEST
{}
RESPONS
{
  "type": "object",
    "properties": {
      "id":{"type":"int"},
      "nickname": { "type": "string"}
    }
  }
}


//PUT/api/users/{id}
REQUEST
{
  "type": "object",
  "properties": {
    "isActive": {
      "type": "boolean"
    }
  },
  "required": ["isActive"]
}
RESPONES
{
  "type": "object",
  "properties": {
    "id": {
      "type": "int"
    },
    "isActive": {
      "type": "boolean"
    }
  },
  "required": ["id", "isActive"]
}
//DELETE/api/users/{id}
REQUEST
{
    "type": "object",
        "properties":{
            "id":"type":"int"
            },
}
RESPONSE
{
    "type": "object",
        "properties":{
        "id":"type":"int"},
        "required": ["id"]
}


