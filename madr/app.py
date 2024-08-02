from http import HTTPStatus

from fastapi import FastAPI

from madr.routers import (
    accounts_router,
    auth_router,
    books_router,
    novelists_router,
)
from madr.schemas.message_schema import MessageSchema

tags_metadata = [
    {
        'name': 'Accounts',
        'description': 'Create and manage users accounts.',
    },
    {
        'name': 'Books',
        'description': 'Manage and add novelist books.',
    },
    {
        'name': 'Novelists',
        'description': 'Manage and add novelist writers.',
    },
    {
        'name': 'Auth',
        'description': "Manage all user's security.",
    },
]

app = FastAPI(
    title='MADR',
    openapi_tags=tags_metadata,
    swagger_ui_parameters={'defaultModelsExpandDepth': 0},
)

app.include_router(accounts_router.router)
app.include_router(books_router.router)
app.include_router(novelists_router.router)
app.include_router(auth_router.router)


@app.get(
    '/',
    status_code=HTTPStatus.OK,
    response_model=MessageSchema,
    include_in_schema=False,
)
def read_root():
    return {'message': 'MADR Online!'}
