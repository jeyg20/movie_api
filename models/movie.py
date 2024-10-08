from pydantic import BaseModel, Field


class Movie(BaseModel):
    id: int | None = None
    title: str | None = Field(default=None, min_length=2, max_length=50)
    overview: str | None = Field(default=None, min_length=2, max_length=350)
    year: int | None = Field(default=None, ge=1800, le=2024)
    rating: float | None = Field(default=None, ge=1, le=10)
    category: str | None = Field(default=None, min_length=1, max_length=50)

    model_config = {
        "json_schema_extra": {
            "example": {
                "id": 1,
                "title": "My movie",
                "overview": "Movie overview",
                "year": 2024,
                "rating": 1,
                "category": "action",
            }
        }
    }

    model_config = {"from_attributes": True}
