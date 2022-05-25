from django.contrib import admin
from django.urls import path, include

from . import views
from .views import index, AddBookView, author_add, year_add, genre_add, detail, authors, genres, search, author_detail, \
    genre_detail

urlpatterns = [
    path('', index, name='index'),
    path('main_page/', index, name='main_page'),
    path('add/', AddBookView.as_view(), name='add'),
    path('add_author/', author_add, name='add_author'),
    path('add_year/', year_add, name='add_year'),
    path('add_genre/', genre_add, name='add_genre'),
    path('detail/<int:book_id>', detail, name='detail'),
    path('author/<str:author_id>', author_detail, name='author_detail'),
    path('genres/<str:genre_id>', genre_detail, name='genre_detail'),
    path('authors/', authors, name='authors'),
    path('genres/', genres, name='genres'),
    path('search/', search, name='search'),
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
]
