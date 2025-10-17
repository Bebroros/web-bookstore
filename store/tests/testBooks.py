import pytest
from django.template.defaultfilters import title
from store.models import Book, Author, Publisher


@pytest.mark.django_db
def test_get_empty_books(api_client):
    response = api_client.get('/books/')
    assert response.status_code == 200
    assert response.json() == []


@pytest.mark.django_db
def test_get_books_unauthenticated(api_client, book):
    response = api_client.get('/books/')

    assert response.status_code == 200
    assert len(response.data) == 1


@pytest.mark.django_db
def test_get_book(api_client, user, book):
    response = api_client.get(f'/books/{book.id}/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_bad_get_book(api_client, user, book):
    response = api_client.get(f'/books/9999999/')
    assert response.status_code == 404


@pytest.mark.django_db
def test_post_book(api_client, user, book, publisher, author, authenticate):
    response = api_client.post('/books/', {'name': 'test',
                                                'description': 'test',
                                                'genre': 'test',
                                                'price': 100,
                                                'publisher': publisher.pk,
                                                'author': author.pk,
                                                'year': 1234
                                                }, format="json")
    assert response.status_code == 201
    assert response.json()['name'] == 'test'
    assert response.json()['author'] == author.pk


@pytest.mark.django_db
def test_bad_post_book(api_client, user, book, publisher, author, authenticate):
    response = api_client.post('/books/', {'name': 'test',
                                                'description': 'test',
                                                'genre': 'test',
                                                'author': author.pk,
                                                'year': 1234
                                                }, format="json")
    assert response.status_code == 400


@pytest.mark.django_db
def test_post_noauth_book(api_client, user, book, publisher, author):
    response = api_client.post('/books/', {'name': 'test',
                                                'description': 'test',
                                                'genre': 'test',
                                                'author': author.pk,
                                                'year': 1234
                                                }, format="json")
    assert response.status_code == 401


@pytest.mark.django_db
def test_put_book(api_client, user, book, publisher, author, authenticate):
    response = api_client.put(f'/books/{book.id}/', {'name': 'NEW_NAME'}, format="json")
    assert response.status_code == 200
    assert response.data['name'] == 'NEW_NAME'


@pytest.mark.django_db
def test_put_unexisting_book(api_client, user, book, publisher, author, authenticate):
    response = api_client.put(f'/books/9999/', {'name': 'NEW_NAME'}, format="json")
    assert response.status_code == 404


@pytest.mark.django_db
def test_bad_put_book(api_client, user, book, publisher, author, authenticate):
    response = api_client.put(f'/books/{book.id}/', {'price': '123lll123dsav'}, format="json")
    assert response.status_code == 400


@pytest.mark.django_db
def test_put_noauth_book(api_client, user, book, publisher, author):
    response = api_client.put(f'/books/{book.id}/', {'name': 'NEW_NAME'}, format="json")
    assert response.status_code == 401


@pytest.mark.django_db
def test_delete_book(api_client, user, book, publisher, author, authenticate):
    response = api_client.delete(f'/books/{book.id}/')
    assert response.status_code == 204


@pytest.mark.django_db
def test_delete_unexisting_book(api_client, user, book, publisher, author, authenticate):
    response = api_client.delete(f'/books/9999999/')
    assert response.status_code == 404


@pytest.mark.django_db
def test_delete_noauth_book(api_client, user, book, publisher, author):
    response = api_client.delete(f'/books/{book.id}/')
    assert response.status_code == 401
