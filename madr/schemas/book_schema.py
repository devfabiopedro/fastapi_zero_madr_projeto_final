from pydantic import BaseModel


class BookSchema(BaseModel):
    year: int
    title: str
    novelist_id: int
