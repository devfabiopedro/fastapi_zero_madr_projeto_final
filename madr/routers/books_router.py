from http import HTTPStatus

from fastapi import APIRouter

from madr.schemas.book_schema import BookSchema

router = APIRouter(prefix='/books', tags=['Books'])


@router.post(
    '/new',
    status_code=HTTPStatus.CREATED,
    response_model=BookSchema,
    name='Create a new Book',
)
def create_book(): ...
