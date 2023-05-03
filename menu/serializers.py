from rest_framework import serializers
from .models import *

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'description', 'photo', 'price',
                  'category', 'visible', 'lactose_free', 'gluten_free', 'vegan']
        

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'description', 'visible']


class MenuSerializer(serializers.HyperlinkedModelSerializer):
    # TODO: Implement a different serializer that displays each item inside its parent category
    pass