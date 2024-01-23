from rest_framework import serializers
from .models import Book
from authors.serializer import AuthorSerializer
class BookSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Book
        fields = ['id', 'title', 'publish_year', 'author', 'barcode']

    def to_representation(self, instance):
        # Override the to_representation method to exclude author's ID
        representation = super().to_representation(instance)
        representation.pop('id', None)
        representation['author'] = instance.author.name
        return representation

class BookByIdSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    class Meta:
        model = Book
        fields = ['id', 'title', 'publish_year', 'author', 'barcode']

    def to_representation(self, instance):
        # Override the to_representation method to exclude author's ID
        representation = super().to_representation(instance)
        representation['author'].pop('id', None)
        return representation
