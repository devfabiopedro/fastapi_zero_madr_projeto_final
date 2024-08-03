import re
import unicodedata
from http import HTTPStatus
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from madr.database import get_session
from madr.models import Account
from madr.schemas.account_schema import (AccountListSchema,
                                         AccountPublicSchema, AccountSchema)
from madr.schemas.message_schema import MessageSchema
from madr.security import get_current_user, get_password_hash
from madr.utils import sanitize_text

router = APIRouter(prefix='/accounts', tags=['Accounts'])

T_Session = Annotated[Session, Depends(get_session)]
T_CurrentUser = Annotated[Account, Depends(get_current_user)]


@router.post(
    '/user',
    status_code=HTTPStatus.CREATED,
    response_model=AccountPublicSchema,
    name='Create an new Account User',
)
def create_user(user: AccountSchema, session: T_Session):
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

    hashed_password = get_password_hash(user.password)

    db_user = Account(
        username= sanitize_text(user.username), 
        email=sanitize_text(user.email), 
        password=hashed_password
    )
    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    return db_user


@router.get(
    '/list',
    status_code=HTTPStatus.OK,
    response_model=AccountListSchema,
    name='Read and list all Users Accounts',
)
def read_users(session: T_Session, skip: int = 0, limit: int = 100):
    users = session.scalars(select(Account).offset(skip).limit(limit)).all()
    total_users = session.query(Account).count()
    return {'accounts': users, 'total': total_users}


@router.put(
    '/user/{user_id}',
    response_model=AccountPublicSchema,
    name='Update an User Data',
)
def update_user(
    user_id: int,
    user: AccountSchema,
    session: T_Session,
    current_user: T_CurrentUser,
):
    if current_user.id != user_id:
        raise HTTPException(
            status_code=HTTPStatus.FORBIDDEN, detail='Not enough permissions'
        )

    current_user.username = sanitize_text(user.username)
    current_user.email = sanitize_text(user.email)
    current_user.password = get_password_hash(user.password)
    session.commit()
    session.refresh(current_user)

    return current_user


@router.delete(
    '/user/{user_id}',
    response_model=MessageSchema,
    name='Delete an User Account',
)
def delete_user(
    user_id: int,
    session: T_Session,
    current_user: T_CurrentUser,
):
    if current_user.id != user_id:
        raise HTTPException(
            status_code=HTTPStatus.FORBIDDEN, detail='Not enough permissions'
        )

    session.delete(current_user)
    session.commit()

    return {'message': 'Account deleted'}
