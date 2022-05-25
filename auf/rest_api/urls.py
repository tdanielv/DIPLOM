
from django.urls import path

from .views import hola_api, hola2, hola3, relation, relation2, producer_detail, production_detail

app_name = 'rest_api'

urlpatterns = [
    path('hola/', hola_api, name='hola'),
    path('hola2/', hola2, name='hola2'),
    path('hola3/', hola3, name='hola3'),
    path('relation/', relation, name='relation'),
    path('relation2/', relation2, name='relation2'),
    path('producer_detail/<int:id>', producer_detail, name='producer_detail'),
    path('production_detail/<int:id>', production_detail, name='production_detail'),
]