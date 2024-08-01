from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from madr.database import get_session
from madr.models import Account
from madr.schemas.account_schema import (
    AccountListSchema,
    AccountPublicSchema,
    AccountSchema,
)
from madr.schemas.message_schema import MessageSchema

router = APIRouter(prefix='/accounts', tags=['Accounts'])


@router.post(
    '/user',
    status_code=HTTPStatus.CREATED,
    response_model=AccountPublicSchema,
)
def create_user(user: AccountSchema, session: Session = Depends(get_session)):
    db_user = session.scalar(
        select(Account).where(
            (Account.username == user.username) | (Account.email == user.email)
        )
    )

    if db_user:
        if db_user.username == user.username:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail='Username already exists',
            )
        elif db_user.email == user.email:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail='Email already exists',
            )

    db_user = Account(
        username=user.username, password=user.password, email=user.email
    )
    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    return db_user


@router.get(
    '/list',
    status_code=status.HTTP_200_OK,
    response_model=AccountListSchema,
    name='Read and list all Accounts',
)
def read_users(
    skip: int = 0, limit: int = 100, session: Session = Depends(get_session)
):
    users = session.scalars(select(Account).offset(skip).limit(limit)).all()
    total_users = session.query(Account).count()
    return {'accounts': users, 'total': total_users}


@router.put('/user/{user_id}', response_model=AccountPublicSchema)
def update_user(
    user_id: int, user: AccountSchema, session: Session = Depends(get_session)
):

    db_user = session.scalar(select(Account).where(Account.id == user_id))
    if not db_user:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User accont not found'
        )

    db_user.username = user.username
    db_user.password = user.password
    db_user.email = user.email
    session.commit()
    session.refresh(db_user)

    return db_user


@router.delete('/user/{user_id}', response_model=MessageSchema)
def delete_user(user_id: int, session: Session = Depends(get_session)):
    db_user = session.scalar(select(Account).where(Account.id == user_id))

    if not db_user:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User account not found'
        )

    session.delete(db_user)
    session.commit()

    return {'message': 'Account deleted'}
