// GET/api/tasks
REQUEST
{}
RESPONSE
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "id": {
        "type": "integer"
      },
      "creator": {
        "type": "string"
      },
      "title": {
        "type": "string"
      },
      "desc": {
        "type": "string"
      },
      "assigned": {
        "type": "array",
        "items": {
          "type": "string"
        }
      },
      "createdAt": {
        "type": "string",
        "format": "date-time"
      }
    },
    "required": [
      "id",
      "creator",
      "title",
      "desc",
      "assigned",
      "createdAt"
    ]
  }
}

//PUT/api/tasks/{id}/complete
REQUEST
{}
RESPONSE
{
  "type": "object",
  "properties": {
    "id": {
      "type": "integer"
    },
    "status": {
      "type": "string"
    }
  },
  "required": ["id", "status"]
}
//POST/api/tasks/{id}/assign
REQUEST
{
  "type": "object",
  "properties": {
    "userId": {
      "type": "integer"
    }
  },
  "required": ["userId"]
}
RESPONSE
{
  "type": "object",
  "properties": {
    "id": {
      "type": "integer"
    },
    "assigned": {
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  },
  "required": ["id", "assigned"]
}
//GET/api/tasks/{id}
REQUEST
{}
RESPONSE
{   "type":"object",
    "properties": {
      "id": {
        "type": "integer"
      },
      "creator": {
        "type": "string"
      },
      "title": {
        "type": "string"
      },
      "desc": {
        "type": "string"
      },
      "assigned": {
        "type": "array",
        "items": {
          "type": "string"
        }
      },
      "createdAt": {
        "type": "string",
        "format": "date-time"
      }
    },
    "required": [
      "id",
      "creator",
      "title",
      "desc",
      "assigned",
      "createdAt"
    ]
  }

 //POST/api/tasks/
 REQUEST
{
  "type": "object",
  "properties": {
    "title": {
      "type": "string",
      "maxLength": 200
    },
    "desc": {
      "type": "string",
      "maxLength": 20000
    }
  },
  "required": ["title", "desc"]
}
 RESPONSE
{
  "type": "object",
  "properties": {
    "id": {
      "type": "integer"
    },
    "creator": {
      "type": "string"
    },
    "title": {
      "type": "string"
    },
    "desc": {
      "type": "string"
    },
    "createdAt": {
      "type": "string",
      "format": "date-time"
    }
  },
  "required": [
    "id",
    "creator",
    "title",
    "desc",
    "createdAt"
  ]
}
  //PUT/api/tasks/{id}
 REQUEST
{
  "type": "object",
  "properties": {
    "title": {
      "type": "string",
      "maxLength": 200
    },
    "desc": {
      "type": "string",
      "maxLength": 20000
    }
  },
  "required": ["title", "desc"]
}
 RESPONSE
 {
   "type": "object",
   "properties": {
     "id": {
       "type": "integer"
     },
     "title": {
       "type": "string"
     },
     "desc": {
       "type": "string"
     }
   },
   "required": ["id", "title", "desc"]
 }
 //DELETE/api/tasks/{id}
REQUEST
{}
RESPONSE
{}

