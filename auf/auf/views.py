

from django.http import HttpResponse
from django.shortcuts import render


def startpage(request):
    return render(request, 'start_page.html')