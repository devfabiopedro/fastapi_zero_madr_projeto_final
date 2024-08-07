from http import HTTPStatus


def test_deny_create_book_without_permissions(client):
    response = client.post(
        '/books/new',
        json={
            'year': '2024',
            'title': 'Como ser um melhor praticante de programação!',
            'novelist_id': 1,
        },
    )
    assert response.status_code == HTTPStatus.UNAUTHORIZED


def test_allow_create_book_with_permissions(client, token):
    response = client.post(
        '/books/new',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'year': '2024',
            'title': 'Como ser um melhor praticante de programação!',
            'novelist_id': 1,
        },
    )
    data = response.json()
    ...
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'year': '2024',
        'title': data['title'],
        'novelist_id': 1,
    }


def test_get_one_book(client, book):
    response = client.get(f'/books/{book.id}')
    assert response.status_code == HTTPStatus.OK


def test_get_one_inexitent_book(client):
    response = client.get('books/1')
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Livro não consta no MADR'}


def test_list_all_books_but_list_empty(client):
    response = client.get('books/list')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'books': [],
        'total': 0,
        'page': 1,
        'per_page': 20,
        'total_pages': 0,
    }


def test_list_all_books_list_with_book(client, book):
    response = client.get('books/list')
    assert response.status_code == HTTPStatus.OK

    response_data = response.json()
    assert 'books' in response_data
    assert len(response_data['books']) > 0
    assert response_data['books'][0]['id'] == book.id


def test_if_book_exists(client, book, token):
    response = client.post(
        '/books/new',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'year': book.year,
            'title': book.title,
            'novelist_id': book.novelist_id,
        },
    )
    ...
    assert response.status_code == HTTPStatus.CONFLICT
    assert response.json() == {'detail': 'Livro já consta no MADR'}


def test_read_books_filter_by_title(client, book):
    response = client.get(
        '/books/list',
        params={'title': book.title, 'year': book.year},
    )
    assert response.status_code == HTTPStatus.OK
    data = response.json()
    assert len(data['books']) == 1
    assert data['books'][0]['title'] == book.title
    assert data['books'][0]['year'] == book.year


def test_patch_book_error(client, token):
    response = client.patch(
        '/books/1',
        json={
            'year': 'string',
            'title': 'string',
            'novelist_id': 0,
        },
        headers={'Authorization': f'Bearer {token}'},
    )
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Livro não consta no MADR'}


def test_patch_book(client, book, token):
    response = client.patch(
        f'/books/{book.id}',
        json={
            'year': 'string',
            'title': 'um livro qualquer!',
            'novelist_id': 0,
        },
        headers={'Authorization': f'Bearer {token}'},
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json()['title'] == 'um livro qualquer!'


def test_delete_book(client, book, token):
    response = client.delete(
        f'/books/{book.id}',
        headers={
            'Authorization': f'Bearer {token}',
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Livro deletado no MADR'}


def test_delete_book_error(client, token):
    response = client.delete(
        '/books/2', headers={'Authorization': f'Bearer {token}'}
    )
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Livro não consta no MADR'}
