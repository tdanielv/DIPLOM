from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import BBooks, Album, Pep, Producer, Production
from .serializers import BBooksSerializers, AlbumSerializer, PepSerializer, ProducersSerializer, ProductionsSerializer


# @api_view(['GET'])
# def hola_api(request):
#     if request.method == 'GET':
#         b = BBooks.objects.all()
#         serializer = BBooksSerializers(b, many=True)
#         return Response(serializer.data)

@api_view(['GET', 'POST'])
def hola_api(request):
    # books = BBooks.objects.all()
    # serializer = BBooksSerializers(books, many=True)



    if request.method == 'GET':
        bbooks = BBooks.objects.all()
        serializer = BBooksSerializers(bbooks, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        print('REQUEST.DATA', request.data)
        bbooks = request.data
        title=request.data.get('title')
        genre=request.data.get('genre')
        year=request.data.get('year')
        print('TITLE DATA', title)
        print('GENRE DATA', genre)
        print('YEAR DATA', year)
        serr=BBooksSerializers(data=bbooks)

        if serr.is_valid():
            serr.save()
            return Response({'Success': ' created succesfully'})
        else:
            return Response({'Error':'Errorrrr'})
    # return Response(serializer2.data)

@api_view(['GET', 'POST'])
def hola2(request):
        # books = BBooks.objects.all()
        # serializer = BBooksSerializers(books, many=True)

    if request.method == 'GET':
        album = Album.objects.all()
        serializer = AlbumSerializer(album, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        album = request.data
        serr = BBooksSerializers(data=album)

        if serr.is_valid():
            serr.save()
            return Response({'Success': ' created succesfully'})
        else:
            return Response({'Error': 'Errorrrr'})
@api_view(['GET', 'POST'])
def hola3(request):
        # books = BBooks.objects.all()
        # serializer = BBooksSerializers(books, many=True)

    if request.method == 'GET':
        pep = Pep.objects.all()
        serializer = PepSerializer(pep, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        pep = request.data
        serr = PepSerializer(data=pep)

        if serr.is_valid():
            serr.save()
            return Response({'Success': ' created succesfully'})
        else:
            return Response({'Error': 'Errorrrr'})


def relation(request):
    producers = Producer.objects.all()
    print(producers)
    for producer in producers:
        prod = producer.productions.all()
        # print(prod, producer)
    productions = Production.objects.all()
    print(productions)
    context = {'producers': producers, 'productions': productions}
    return render(request, 'relation.html', context)

@api_view(['GET'])
def relation2(request):
    producers = Producer.objects.all()
    productions = Production.objects.all()
    serializer1 = ProducersSerializer(producers, many=True)
    serializer2 = ProductionsSerializer(productions, many=True)
    return Response(serializer2.data)

def producer_detail(request, id):
    producer = Producer.objects.get(id=id)
    p = producer.producers.all()
    context = {'products': p, 'producer': producer}
    return render(request, 'producer_detail.html', context)

def production_detail(request, id):
    product = Production.objects.get(id=id)
    p = product.productions.all()
    context = {'producers': p, 'product': product}
    return render(request, 'production_detail.html', context)


