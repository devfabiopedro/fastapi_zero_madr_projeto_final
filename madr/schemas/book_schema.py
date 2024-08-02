from pydantic import BaseModel


class BookSchema(BaseModel):
    year: int
    title: str
    novelist_id: int


class ListBooksSchema(BaseModel):
    books: list[BookSchema]
