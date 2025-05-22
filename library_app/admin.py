from django.contrib import admin
from .models import User, Book
from django.contrib.auth.admin import UserAdmin

@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Aditional Infortmation', {'fields': ('rol', 'borrowed_book')}),
    )

admin.site.register(Book)