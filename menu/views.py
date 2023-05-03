from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

from .models import *
from .serializers import *
from rest_framework import viewsets, permissions

# Create your views here.

def index(request):
    return HttpResponse("Menu")


def get_items_by_category(request, category_id):
    category = Category.objects.filter(id=category_id).first()

    if not category or not category.visible:
        return HttpResponseNotFound("Ops! Parece que essa categoria não existe!") # TODO: Set custom 404

    items = Item.objects.filter(category=category, visible=True)

    return HttpResponse(items)

# API endpoints

class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class MenuViewSet(viewsets.ModelViewSet):
    pass

