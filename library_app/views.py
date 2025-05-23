from .forms import RegisterUserForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

def user_registration(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuario registrado correctamente")
            return redirect('login')
        else:
            form = RegisterUserForm()
    return render(request, 'auth/registration.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.rol == 'admin':
                return redirect('dashboard')
            else:
                return redirect('index')
        else:
            messages.error(request, 'Nombre de usuario o contraseña inválidos.')
    return render(request, 'auth/login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')