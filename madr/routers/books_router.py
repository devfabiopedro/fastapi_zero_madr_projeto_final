from http import HTTPStatus
from typing import Annotated, Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from madr.database import get_session
from madr.models import Account, Book
from madr.schemas.book_schema import (
    BookPublicSchema,
    BookSchema,
    PaginatedBooksResponse,
)
from madr.security import get_current_user

router = APIRouter(prefix='/books', tags=['Books'])

T_Session = Annotated[Session, Depends(get_session)]
T_CurrentUser = Annotated[Account, Depends(get_current_user)]


@router.post(
    '/new',
    status_code=HTTPStatus.CREATED,
    response_model=BookSchema,
    name='Create a new Book',
)
def create_book(
    book: BookSchema,
    session: T_Session,
    current_user: T_CurrentUser,
):
    db_book = session.scalar(
        select(Book).where(Book.title == book.title.lower())
    )

    if db_book:
        raise HTTPException(
            status_code=HTTPStatus.CONFLICT,
            detail='Livro já consta no MADR',
        )

    db_book = Book(
        year=book.year, title=book.title.lower(), novelist_id=book.novelist_id
    )

    session.add(db_book)
    session.commit()
    session.refresh(db_book)

    return db_book


@router.get(
    '/list',
    status_code=HTTPStatus.OK,
    response_model=PaginatedBooksResponse,
    name='Read and list all Books',
)
def read_books(
    session: T_Session,
    title: Optional[str] = None,
    year: Optional[int] = None,
    page: int = 1,
    per_page: int = 20,
):
    query = session.query(Book)

    if title:
        query = query.filter(Book.title.ilike(f'%{title}%'))
    if year:
        query = query.filter(Book.year == year)

    total_books = query.count()

    query = query.offset((page - 1) * per_page).limit(per_page)

    books = query.all()

    return {
        'books': books,
        'total': total_books,
        'page': page,
        'per_page': per_page,
        'total_pages': (total_books + per_page - 1) // per_page,
    }


@router.get(
    '/{book_id}',
    status_code=HTTPStatus.OK,
    response_model=BookPublicSchema,
    name='Find one Book by id',
)
def read_one_book(book_id: int, session: T_Session):
    book = session.scalar(select(Book).where((Book.id == book_id)))

    if not book:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Livro não consta no MADR'
        )

    return book


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
