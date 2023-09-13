from src.db.schemas.model_schema import ModelSchema


class SongSchema(ModelSchema):
    bson_type: str = "object"
    required: list = [
        "id",
        "title",
        "artist",
        "genre",
        "release_year",
        "popularity",
        "available_on",
        "created_at",
        "cover",
    ]
    properties: dict = {
        "id": {"bson_type": "string", "description": "The music's unique identifier"},
        "title": {"bson_type": "string", "description": "The title of the music"},
        "artist": {"bson_type": "string", "description": "The artist of the music"},
        "genre": {"bson_type": "string", "description": "The genre of the music"},
        "release_year": {
            "bson_type": "integer",
            "description": "The release year of the music",
        },
        "popularity": {"bson_type": "integer", "description": "The music's popularity"},
        "available_on": {
            "bson_type": "object",
            "description": "The music's available on",
        },
        "created_at": {
            "bson_type": "string",
            "description": "The music's creation time",
        },
        "cover": {
            "bson_type": "string",
            "description": "The music's cover",
        },
    }

    def get(self) -> dict:
        return {
            "bson_type": self.bson_type,
            "required": self.required,
            "properties": self.properties,
        }
