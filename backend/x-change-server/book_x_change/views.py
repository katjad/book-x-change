from django.shortcuts import render
from django.http import JsonResponse
from django.core.serializers import serialize
from .models import Book

def index(request):
    books = Book.objects.all()
    return JsonResponse(serialize('json', books), safe=False)
