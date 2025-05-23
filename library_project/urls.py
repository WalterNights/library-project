from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('auth/', include('library_app.urls')),
    path('api/', include('library_app.api_urls')),
]