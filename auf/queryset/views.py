from django.shortcuts import render

from .django_fun import query_debugger, book_list, book_list_select_related
from .models import Book, Publisher


def query_set_view(request):
    query_set = Publisher.objects.prefetch_related('book_set')
    print(query_set)
    context = {'books': query_set}
    return render(request, 'queryset.html', context)