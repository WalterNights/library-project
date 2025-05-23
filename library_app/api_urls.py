from . import api_views
from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('books/', api_views.BookListCreateAPIView.as_view(), name='api_books'),
    path('books/<int:pk>/', api_views.BookDetailAPIView.as_view(), name='api_book_detail'),
    path('books/<int:pk>/lend/', api_views.lend_book, name='api_lend_book'),
    path('books/<int:pk>/return/', api_views.return_book, name='api_return_book'),
    path('books/bulk_upload/', api_views.bulk_upload_books, name='api_bulk_upload_books'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]