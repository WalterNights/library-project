from .forms import RegisterUserForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class RegisterUserApiView(APIView):
    def post(self, request):
        form = RegisterUserForm(request.data)
        if form.is_valid():
            form.save()
            return Response({'detail': 'Usuario registrado correctamente'}, status=status.HTTP_201_CREATED)
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)