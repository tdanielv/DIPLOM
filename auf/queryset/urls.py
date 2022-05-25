from django.urls import path

from .views import query_set_view

urlpatterns = [
    path('', query_set_view, name='query_set_view')
]