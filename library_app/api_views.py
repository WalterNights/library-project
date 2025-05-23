import pandas as pd
from .models import Book
from rest_framework import status
from .serializers import BookSerializer
from rest_framework.response import Response
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated, IsAdminUser
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
    return Response({'mensaje': f'{book.title} Prestado correctamente.'})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def return_book(request, pk):
    user = request.user
    book = Book.objects.get(pk=pk)
    user.borrowed_book.remove(Book)
    return Response({'mensaje': f'{book.title} Devuelto correctamente.'})

@api_view(['POST'])
@permission_classes([IsAdminUser])
def bulk_upload_books(request):
    excel_file = request.FILES.get('file')
    if not excel_file:
        return Response({'error': 'No se ha proporcionado un archivo Excel.'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        df = pd.read_excel(excel_file)
        books = [
            Book(
                title=row['titulo'],
                author=row['autor'],
                year_publication=row['año de publicación'],
                stock=row['cantidad disponible']
            )
            for _, row in df.iterrows()
        ]
        Book.objects.bulk_create(books)
        return Response({'mensaje': 'Libros subidos correctamente.'}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)