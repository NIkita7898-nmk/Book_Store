from rest_framework import serializers
from django.utils import timezone
from .models import Information
from books.models import Book

class InformationSerializer(serializers.ModelSerializer):
    book = Book()
    class Meta:
        model = Information
        fields = ['book', 'quantity']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['book'] = instance.book.title
        return representation

    def create(self, validated_data):
        validated_data['created_at'] = timezone.now()
        return super().create(validated_data)

        
class InformationHistorySerializer(serializers.ModelSerializer):
    book = serializers.SerializerMethodField()
    history = serializers.SerializerMethodField()

    class Meta:
        model = Information
        fields = ['book', 'history']

    def get_book(self, obj):
        book = Book.objects.get(id=obj.id)
        return {'key': book.id, 'title': book.title}

    def get_history(self, obj):
        book = Book.objects.get(id=obj.id)
        information_history = Information.objects.filter(book=book.id).order_by('-created_at')
        history_list = [{'date': entry.created_at, 'quantity': entry.quantity} for entry in information_history]
        return history_list
