from http import HTTPStatus


def test_allow_create_book_with_permissions(client, token):
    response = client.post(
        '/books/new',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'year': 2024,
            'title': 'Como ser um melhor praticante de programação!',
            'novelist_id': 1,
        },
    )
    data = response.json()
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'year': 2024,
        'title': data['title'],
        'novelist_id': 1,
    }

def test_deny_create_book_without_permissions(client):
    response = client.post(
        '/books/new',
        json={
            'year': 2024,
            'title': 'Como ser um melhor praticante de programação!',
            'novelist_id': 1,
        },
    )
    assert response.status_code == HTTPStatus.UNAUTHORIZED
