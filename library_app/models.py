from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser, BaseUserManager

class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('rol', 'user')
        if not email:
            raise ValueError('El usuario debe tener un correo electrónico')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('rol', 'admin')
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superusuario debe tener is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superusuario debe tener is_siperuser=True')
        
        return self.create_user(username, email, password, **extra_fields)


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    year_publication = models.CharField(max_length=4)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return (f'{self.title} - {self.author} - {self.year_publication}')
   
    
class User(AbstractUser):
    ROL_CHOICES = (
        ('user', 'Usuario Regular'),
        ('admin', 'Administrador'),
    )
    rol = models.CharField(max_length=10, choices=ROL_CHOICES, default='user')
    borrowed_book = models.ManyToManyField(Book, blank=True, related_name='user_with_book')

    objects = UserManager()

    def __str__(self):
        return self.username
    
class LoanHistory(models.Model):
    ACTION_CHOICES = (
        ('borrow', 'Préstamo'),
        ('return', 'Devolución'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    action = models.CharField(max_length=10, choices=ACTION_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.book.title} - {self.action} - {self.timestamp}'