from rest_framework import serializers

from ..models import Book


class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    author = serializers.CharField()
    description = serializers.CharField()
    stock = serializers.BooleanField()

    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.author = validated_data.get('author', instance.author)
        instance.description = validated_data.get('description', instance.description)
        instance.stock = validated_data.get('stock', instance.stock)
        instance.save()
        return instance


