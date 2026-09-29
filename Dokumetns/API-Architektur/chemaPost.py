// GET/api/posts
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
      "nickname": {
        "type": "string"
      },
      "title": {
        "type": "string"
      },
      "desc": {
        "type": "string"
      }
      "url":{
        "type": "string",
        "format": "uri"
      },
      "createdAt":{
        "type":"string",
        "format": "date-time"
    },
    "required": ["id", "nickname", "title", "desc","url","createdAt"]
  }
}
//GET//api/posts/{id}
REQUEST
{}
RESPONSE
{
  "type": "object",
  "properties": {
    "id": {
      "type": "integer"
    },
    "nickname": {
      "type": "string"
    },
    "title": {
      "type": "string"
    },
    "desc": {
      "type": "string"
    },
    "url": {
      "type": "string",
      "format":"uri"
    },
    "createdAt":{
            "type":"string",
            "format": "date-time"
    },
  "required": ["id", "nickname", "title", "desc", "url","createdAt"]
}

//POST/api/posts
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
    },
    "url": {
      "type": "string",
      "format": "uri"
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
    },
    "url": {
      "type": "string",
      "format": "uri"
    },
    "createdAt": {
      "type": "string",
      "format": "date-time"
    }
  },
  "required": ["id", "title", "desc", "createdAt"]
}
//PUT/api/posts{id}
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
    },
    "url": {
      "type": "string",
      "format": "uri"
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
    },
    "url": {
      "type": "string",
      "format": "uri"
    }
  },
  "required": ["id", "title", "desc"]
}
//DELETE/api/posts{id}
REQUEST
{}
RESPONSE
{}
//
