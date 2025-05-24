from .models import User, Book
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model: User
        fields = ['id', 'username', 'email', 'rol', 'borrowed_book']