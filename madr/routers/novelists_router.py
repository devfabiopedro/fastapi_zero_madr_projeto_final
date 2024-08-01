from fastapi import APIRouter, status

from madr.schemas.novelist_schema import NovelistSchema

router = APIRouter(prefix='/novelists', tags=['Novelists'])


@router.get(
    '/',
    status_code=status.HTTP_200_OK,
    response_model=NovelistSchema,
    name='Read and list all Novelists',
)
def read_novelists(): ...
