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

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
class MenuViewSet(viewsets.ModelViewSet):
    """Complete menu visualization"""
    # TODO: Implement
    pass

from rest_framework import generics

class CategoryList(generics.ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset = Category.objects.all()
        return queryset

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['include_items'] = True
        return context
