from rest_framework import serializers as sz
from .models import Tag


class TagSerializer(sz.ModelSerializer):
    """Serializer for tag objects"""
    class Meta:
        model = Tag
        fields = ('id', 'name')
        read_only_fields = ('id',)
