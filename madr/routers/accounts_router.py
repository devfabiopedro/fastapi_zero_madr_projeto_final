from fastapi import APIRouter, status

from madr.schemas import AccountSchema

router = APIRouter(prefix='/account', tags=['Account'])


@router.get(
    '/',
    status_code=status.HTTP_200_OK,
    response_model=AccountSchema,
    name='Read and list all Accounts',
)
def read_users(): ...
