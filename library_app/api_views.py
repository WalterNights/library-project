import pandas as pd
from rest_framework import status
from .models import User, Book, LoanHistory
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework import generics, permissions
from .serializers import BookSerializer, LoanHistorySerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser


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
    
class UserListCreateAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return User.objects.exclude(rol='admin')
    
@api_view(['GET'])
@permission_classes([IsAdminUser])
def user_loan_history_by_id(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return Response({'error': 'Usuario no encontrado.'}, status=status.HTTP_404_NOT_FOUND)
    
    history = LoanHistory.objects.filter(user=user).order_by('-timestamp')
    serializer = LoanHistorySerializer(history, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def lend_book(request, pk):
    user = request.user
    book = Book.objects.get(pk=pk)
    user.borrowed_book.add(book)
    LoanHistory.objects.create(user=user, book=book, action='borrow')
    book.stock -= 1
    return Response({'mensaje': f'{book.title} Prestado correctamente.'})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def return_book(request, pk):
    user = request.user
    book = Book.objects.get(pk=pk)
    user.borrowed_book.remove(book)
    LoanHistory.objects.create(user=user, book=book, action='return')
    book.stock += 1
    return Response({'mensaje': f'{book.title} Devuelto correctamente.'})

@api_view(['POST'])
@permission_classes([])
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
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_loan_history(request):
    user = request.user
    loan_history = LoanHistory.objects.filter(user=user).order_by('-timestamp')
    serializer = LoanHistorySerializer(loan_history, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)