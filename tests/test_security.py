from http import HTTPStatus

from jwt import decode
from pwdlib import PasswordHash

from madr.security import (
    create_access_token,
    get_password_hash,
    settings,
    verify_password,
)


def test_jwt():
    data = {'test': 'test'}
    token = create_access_token(data)

    decoded = decode(
        token,
        settings.SECRET_KEY,
        algorithms=[settings.ALGORITHM],
    )

    assert decoded['test'] == data['test']
    assert decoded['exp']  # Testa se o valor de exp foi adicionado ao token


def test_make_str_password_in_str_hash():
    hashmaker = PasswordHash.recommended()
    pass_to_hash = 'mypassword'
    pass_hashed = get_password_hash(pass_to_hash)

    assert hashmaker.verify(pass_to_hash, pass_hashed) is True
    assert verify_password(pass_to_hash, pass_hashed) is True


def test_get_token(client, user):
    response = client.post(
        'auth/token',
        data={'username': user.email, 'password': user.clean_password},
    )
    token = response.json()

    assert response.status_code == HTTPStatus.OK
    assert 'access_token' in token
    assert 'token_type' in token


def test_if_jwt_invalid_token(client):
    response = client.delete(
        'accounts/user/1', headers={'Authorization': 'Bearer token-invalido'}
    )
    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Could not validate credentials'}
