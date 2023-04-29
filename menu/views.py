from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

from .models import *

# Create your views here.

def index(request):
    return HttpResponse("Menu")


def get_items_by_category(request, category_id):
    category = Category.objects.filter(id=category_id).first()

    if not category or not category.visible:
        return HttpResponseNotFound("Ops! Parece que essa categoria não existe!")

    return HttpResponse(category)