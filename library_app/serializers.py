from .models import User, Book, LoanHistory
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'rol', 'borrowed_book']
        
class LoanHistorySerializer(serializers.ModelSerializer):
    book_title = serializers.CharField(source='book.title', read_only=True) 
    
    class Meta:
        model = LoanHistory
        fields = ['id', 'book_title', 'action', 'timestamp']