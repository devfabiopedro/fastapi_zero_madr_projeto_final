from datetime import datetime

from pydantic import BaseModel


class BookSchema(BaseModel):
    year: str
    title: str
    novelist_id: int


class BookPublicSchema(BaseModel):
    id: int
    year: str
    title: str
    novelist_id: int
    created_at: datetime
    updated_at: datetime


class PaginatedBooksResponse(BaseModel):
    books: list[BookPublicSchema]
    total: int
    page: int
    per_page: int
    total_pages: int
