from rest_framework import serializers as sz
from .models import Tag, Ingredient, Recipe


class TagSerializer(sz.ModelSerializer):
    """Serializer for tag objects"""
    class Meta:
        model = Tag
        fields = ('id', 'name')
        read_only_fields = ('id',)


class IngredientSerializer(sz.ModelSerializer):
    """Serializer for ingredient objects"""
    class Meta:
        model = Ingredient
        fields = ('id', 'name')
        read_only_fields = ('id',)


class RecipeSerializer(sz.ModelSerializer):
    """Serializer a Recipe"""
    ingredients = sz.PrimaryKeyRelatedField(
        many=True,
        queryset=Ingredient.objects.all()
    )
    tags = sz.PrimaryKeyRelatedField(
        many=True,
        queryset=Tag.objects.all()
    )

    class Meta:
        model = Recipe
        fields = (
            'id',
            'title',
            'ingredients',
            'tags',
            'time_minutes',
            'price',
            'link'
        )
        read_only_fields = ('id',)
