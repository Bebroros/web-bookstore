from django.contrib import admin
from django.urls import path
from store.views import *

app_name = 'store'
urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('books/<int:id>/', BookDetail.as_view(), name='book-detail'),

    path('authors/', AuthorList.as_view(), name='author-list'),
    path('authors/<int:id>/', AuthorDetail.as_view(), name='author-detail'),

    path('publishers/', PublisherList.as_view(), name='publisher-list'),
    path('publishers/<int:id>/', PublisherDetail.as_view(), name='publisher-detail'),
]
