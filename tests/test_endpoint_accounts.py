from http import HTTPStatus

from madr.schemas.account_schema import AccountPublicSchema


def test_create_user(client):
    response = client.post(
        '/accounts/user',
        json={
            'username': 'fernanda',
            'email': 'fernanda@email.com',
            'password': 'fernandasecret',
        },
    )
    data = response.json()
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'fernanda',
        'email': 'fernanda@email.com',
        'id': 1,
        'created_at': data['created_at'],
        'updated_at': data['updated_at'],
    }


def test_read_users(client):
    response = client.get('/accounts/list')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'accounts': [], 'total': 0}


def test_read_users_with_users(client, user):
    user_schema = AccountPublicSchema.model_validate(user).model_dump()
    response = client.get('accounts/list')

    data = response.json()['accounts'][0]
    # Modifiquei os campos abaixo porque o formato de data e hora
    # não combinam entre o momento que gera e o momento em que testa
    user_schema['created_at'] = data['created_at']
    user_schema['updated_at'] = data['updated_at']

    assert response.json() == {'accounts': [user_schema], 'total': 1}


def test_update_user(client, user, token):
    response = client.put(
        f'/accounts/user/{user.id}',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'username': 'adriana',
            'email': 'adriana@email.com',
            'password': 'adrianapassword',
        },
    )
    data = response.json()
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'adriana',
        'email': 'adriana@email.com',
        'id': 1,
        'created_at': data['created_at'],
        'updated_at': data['updated_at'],
    }


def test_delete_user(client, user, token):
    response = client.delete(
        f'/accounts/user/{user.id}',
        headers={'Authorization': f'Bearer {token}'},
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Account deleted'}


def test_update_user_with_wrong_user(client, other_user, token):
    response = client.put(
        f'/accounts/user/{other_user.id}',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'username': 'tester1',
            'email': 'tester1@email.com',
            'password': 'tester1',
        },
    )
    assert response.status_code == HTTPStatus.FORBIDDEN
    assert response.json() == {'detail': 'Not enough permissions'}


def test_delete_user_wrong_user(client, other_user, token):
    response = client.delete(
        f'/accounts/user/{other_user.id}',
        headers={'Authorization': f'Bearer {token}'},
    )
    assert response.status_code == HTTPStatus.FORBIDDEN
    assert response.json() == {'detail': 'Not enough permissions'}
