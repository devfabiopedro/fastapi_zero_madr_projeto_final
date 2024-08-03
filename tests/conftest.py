import factory
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

from madr.app import app
from madr.database import get_session
from madr.models import Account, table_registry
from madr.security import get_password_hash


class UserFactory(factory.Factory):
    class Meta:
        model = Account

    username = factory.Sequence(lambda n: f'Tester{n}')
    email = factory.LazyAttribute(
        lambda obj: f'{obj.username}@email.com'.lower()
    )
    password = factory.LazyAttribute(lambda obj: f'{obj.username}'.lower())


@pytest.fixture
def session():
    engine = create_engine(
        'sqlite:///:memory:',
        connect_args={'check_same_thread': False},
        poolclass=StaticPool,
    )
    table_registry.metadata.create_all(engine)

    with Session(engine) as session:
        yield session

    table_registry.metadata.drop_all(engine)


@pytest.fixture
def client(session):
    def get_session_override():
        return session

    with TestClient(app) as client:
        app.dependency_overrides[get_session] = get_session_override
        yield client

    app.dependency_overrides.clear()


@pytest.fixture
def user(session):
    password = 'tester'
    user = UserFactory(password=get_password_hash(password))

    session.add(user)
    session.commit()
    session.refresh(user)

    # Um 'monkey patch' para os testes
    # não testarem em um hash, mas sim uma senha em texto
    user.clean_password = 'tester'

    return user


@pytest.fixture
def other_user(session):
    password = 'tester'
    user = UserFactory(password=get_password_hash(password))

    session.add(user)
    session.commit()
    session.refresh(user)

    user.clean_password = 'tester'

    return user


@pytest.fixture
def token(client, user):
    response = client.post(
        '/auth/token',
        data={'username': user.email, 'password': user.clean_password},
    )
    return response.json()['access_token']
