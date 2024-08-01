from fastapi import APIRouter, status

from madr.schemas.book_schema import BookSchema

router = APIRouter(prefix='/books', tags=['Books'])


@router.get(
    '/',
    status_code=status.HTTP_200_OK,
    response_model=BookSchema,
    name='Read and list all Books',
)
def read_books(): ...
