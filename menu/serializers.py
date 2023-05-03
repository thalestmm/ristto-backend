from rest_framework import serializers
from .models import *

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'description', 'photo', 'price',
                  'category', 'visible', 'lactose_free', 'gluten_free', 'vegan']
        

class CategorySerializer(serializers.ModelSerializer):
    items = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True,
    ) 
    # FIXME: Show only visible items
    # TODO: Send item information on request
    # ! ↑ For this to work the model must have a 'related_name' attribute on the ForeignKey field

    class Meta:
        model = Category
        fields = ['name', 'description', 'visible', 'items']
