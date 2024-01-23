from rest_framework import serializers
from .models import Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'birth_date']

    def to_representation(self, instance):
        # Override the to_representation method to exclude author's ID
        representation = super().to_representation(instance)
        representation.pop('birth_date')
        return representation

