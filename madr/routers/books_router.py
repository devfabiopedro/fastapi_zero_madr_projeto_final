from http import HTTPStatus
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from madr.database import get_session
from madr.models import Account, Book
from madr.schemas.book_schema import BookSchema
from madr.schemas.message_schema import MessageSchema
from madr.security import get_current_user

# from madr.server.services.book_service import (create_book_service,
#                                                delete_book_service,
#                                                get_book_service,
#                                                get_books_service,
#                                                update_book_service)


router = APIRouter(prefix='/books', tags=['Books'])

T_Session = Annotated[Session, Depends(get_session)]
T_CurrentUser = Annotated[Account, Depends(get_current_user)]

@router.post(
    '/new',
    status_code=HTTPStatus.CREATED,
    response_model=BookSchema,
    name='Create a new Book',
)
def create_book(book: BookSchema, current_user: T_CurrentUser, session: T_Session):
    db_book = session.scalar(
        select(Book).where(Book.title == book.title.lower())
    )

    if db_book:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='The book already exists',
        )

    db_book = Book(
        year=book.year,
        title=book.title.lower(),
        novelist_id=book.novelist_id
    )

    session.add(db_book)
    session.commit()
    session.refresh(db_book)

    return db_book


# @router.delete('/livro/{id}', status_code=status.HTTP_200_OK)
# def delete_book(id: int, current_user: CurrentUser, db: DBSession):
#     delete_book_service(id, db)
#     return Message(message='Livro deletado no MADR')


# @router.patch(
#     '/livro/{id}',
#     status_code=status.HTTP_200_OK,
#     response_model=UpdateBookRequestSchema,
# )
# def update_book(
#     id: int,
#     data: UpdateBookRequestSchema,
#     current_user: CurrentUser,
#     db: DBSession,
# ):
#     new_book = update_book_service(id, data, db)
#     return UpdateBookRequestSchema(
#         id=new_book.id,
#         ano=new_book.year,
#         titulo=new_book.title,
#         romancista_id=new_book.author_id,
#     )


# @router.get(
#     '/livro/{id}',
#     status_code=status.HTTP_200_OK,
#     response_model=GetBookResponseSchema,
# )
# def get_book(id: int, db: DBSession):
#     book = get_book_service({'id': id}, db=db)
#     return GetBookResponseSchema(
#         id=book.id,
#         ano=book.year,
#         titulo=book.title,
#         romancista_id=book.author_id,
#     )


# @router.get(
#     '/livro',
#     status_code=status.HTTP_200_OK,
#     response_model=GetManyBooksResponseSchema,
# )
# def get_books(
#     db: DBSession,
#     year: int | None = Query(None, alias='ano'),
#     title: str | None = Query(None, alias='titulo'),
#     page: int = Query(1, alias='pagina'),
# ):
#     where = {}
#     if year:
#         where['year'] = year
#     if title:
#         where['title'] = title
#     books = get_books_service(where, db, page)
#     books = [
#         GetBookResponseSchema(
#             id=book.id,
#             ano=book.year,
#             titulo=book.title,
#             romancista_id=book.author_id,
#         )
#         for book in books
#     ]
#     return GetManyBooksResponseSchema(livros=books)