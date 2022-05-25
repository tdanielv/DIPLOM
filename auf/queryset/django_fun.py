
from django.db.models import Prefetch, Max
from django.shortcuts import render

from django.db import connection, reset_queries
import time
import functools

from .models import Book, Store


def query_debugger(func):

    @functools.wraps(func)
    def inner_func(*args, **kwargs):

        reset_queries()

        start_queries = len(connection.queries)

        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()

        end_queries = len(connection.queries)

        print(f"Function : {func.__name__}")
        print(f"Number of Queries : {end_queries - start_queries}")
        print(f"Finished in : {(end - start):.2f}s")
        return result

    return inner_func


@query_debugger
def book_list():
    queryset = Book.objects.all()
    books = []
    for book in queryset:
        books.append({'id': book.id, 'name': book.name, 'publisher': book.publisher.name})
    return books

# from queryset.django_fun import book_list
@query_debugger
def book_list_select_related():

    queryset = Book.objects.select_related('publisher').all()
    print(queryset)
    books = []

    for book in queryset:
        books.append({'id': book.id, 'name': book.name, 'publisher': book.publisher.name})

    return books

@query_debugger
def store_list():

    queryset = Store.objects.all()


    stores = []

    for store in queryset:
        books = [book.name for book in store.books.all()]
        stores.append({'id': store.id, 'name': store.name, 'books': books})

    return stores


@query_debugger
def store_list_prefetch_related():
    queryset = Store.objects.prefetch_related('books')

    stores = []

    for store in queryset:
        books = [book.name for book in store.books.all()]
        stores.append({'id': store.id, 'name': store.name, 'books': books})


    return stores


@query_debugger
def store_list_expensive_books_prefetch_related():
    queryset = Store.objects.prefetch_related('books')

    stores = []
    for store in queryset:
        books = [book.name for book in store.books.filter(price__range=(250, 300))]
        stores.append({'id': store.id, 'name': store.name, 'books': books})

    return stores

@query_debugger
def store_list_expensive_books_prefetch_related_efficient():

    queryset = Store.objects.prefetch_related(
        Prefetch('books', queryset=Book.objects.filter(price__range=(250, 300))))

    stores = []
    for store in queryset:
        books = [book.name for book in store.books.all()]
        stores.append({'id': store.id, 'name': store.name, 'books': books})

    return stores
print(store_list_expensive_books_prefetch_related_efficient())
def model_annotate():
    queryset = Book.objects.annotate(Max('price'))
    print(queryset[0].__dict__)
    print(queryset[0].price__max, '10000')
    for book in queryset:
        print(book.__dict__)
