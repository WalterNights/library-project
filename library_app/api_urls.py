from . import api_views
from django.urls import path
from django.http import HttpResponse
from library_app.views import current_user

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

def test_api_view(request):
    return HttpResponse("API Test successful!", status=200)

urlpatterns = [
    path('test/', test_api_view, name='api_test'),
    
    path('books/', api_views.BookListCreateAPIView.as_view(), name='api_books'),
    path('books/<int:pk>/', api_views.BookDetailAPIView.as_view(), name='api_book_detail'),
    path('books/<int:pk>/lend/', api_views.lend_book, name='api_lend_book'),
    path('books/<int:pk>/return/', api_views.return_book, name='api_return_book'),
    path('books/bulk_upload/', api_views.bulk_upload_books, name='api_bulk_upload_books'),
    
    path('users/', api_views.UserListCreateAPIView.as_view(), name='api_users'),
    path('users/me/', current_user, name='current_user'),
    path('users/me/history', api_views.user_loan_history, name='user_loan_history'),
    path('users/<int:user_id>/history', api_views.user_loan_history_by_id, name='user_loan_history_by_id'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]