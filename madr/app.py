from http import HTTPStatus

from fastapi import FastAPI

from madr.routers import accounts_router, books_router, novelists_router
from madr.schemas.message_schema import MessageSchema

app = FastAPI(title='MADR')

app.include_router(accounts_router.router)
app.include_router(books_router.router)
app.include_router(novelists_router.router)


@app.get('/', status_code=HTTPStatus.OK, response_model=MessageSchema)
def read_root():
    return {'message': 'MADR Online!'}
