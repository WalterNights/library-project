from .models import Book
from .serializers import BookSerializer
from rest_framework.response import Response
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]
    
class BookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def lend_book(request, pk):
    user = request.user
    book = Book.objects.get(pk=pk)
    user.borrowed_book.add(Book)
    return Response({'mensaje': f'{book.title} prestado correctamente.'})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def return_book(request, pk):
    user = request.user
    book = Book.objects.get(pk=pk)
    user.borrowed_book.remove(Book)
    return Response({'mensaje': f'{book.title} devuelto correctamente.'})