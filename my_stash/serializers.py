from rest_framework import serializers
from .models import Place, Large_class, Small_class, Item

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = (
            'name',
        )

class ItemSerializer(serializers.ModelSerializer):
    item_place = serializers.StringRelatedField()
    item_small_class = serializers.StringRelatedField()
    item_large_class = serializers.StringRelatedField()
    class Meta:
        model = Item
        fields = (
            'id',
            'item_place',
            'name',
            'item_small_class',
            'item_large_class',
            'is_set',
            'set_name'
        )

class SclassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Small_class
        fields = (
            'name',
        )

class LclassSerializer(serializers.ModelSerializer):
    small_class_set = SclassSerializer(many=True)
    item_set = ItemSerializer(many=True)
    class Meta:
        model = Large_class
        fields = (
            'name',
            'small_class_set',
            'item_set'
        )

class ItemSerializer(serializers.ModelSerializer):
    item_place = serializers.StringRelatedField()
    item_small_class = serializers.StringRelatedField()
    item_large_class = serializers.StringRelatedField()
    class Meta:
        model = Item
        fields = (
            'id',
        	'item_place',
            'name',
            'item_small_class',
            'item_large_class',
            'is_set',
            'set_name'
        )