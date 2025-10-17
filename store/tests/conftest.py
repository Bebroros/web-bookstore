import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from store.models import Author, Publisher, Book


@pytest.fixture(scope='function')
def api_client():
    yield APIClient()


@pytest.fixture(scope='function')
def user():
    yield User.objects.create_user(
        username='staff',
        email='staff1@book.ua',
        password='B00k_5T0r3',
        is_staff=True
    )


@pytest.fixture(scope='function')
def author():
    author = Author.objects.create(name="Test Author", description="Test Description")
    yield author


@pytest.fixture(scope='function')
def publisher():
    publisher = Publisher.objects.create(name="Test Publisher", description="Test Description")
    yield publisher


@pytest.fixture(scope='function')
def book(author, publisher):
    book = Book.objects.create(
        name="Test Book",
        description="Test Description",
        publisher=publisher,
        author=author,
        genre="Test Genre",
        price=444,
        year=1234,
    )
    yield book


@pytest.fixture(scope='function')
def authenticate(api_client, user):
    response = api_client.post(
        '/auth/login/',
        {
            'username': user.username,
            'password': "B00k_5T0r3",
        }, format='json')
    assert response.status_code == 200
    token = response.data['access']
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    yield token
