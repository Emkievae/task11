from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url=reverse_lazy('login'))
# Создаем отображение профиля
def profile_view(request):
    return render(request, 'app_auth/profile.html')

# Cоздаем аутентификацию пользователя
def login_view(request):
    redirect_url = reverse('profile')
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect(redirect_url)
        else:
            return render(request, 'app_auth/login.html')
    
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username, password)
    # проверка, что нашлась комбинация логина и пароля
    if user is not None:
        login(request, user)
        return redirect(redirect_url)
    # комбинация логина и пароля не нашлась - пишем, что пользователь не найден
    return render(request, 'app_auth/login.html', {'error':'Пользователь не найден'})

# Cоздаем выход из профиля
def logout_view(request):
    logout(request)
    return redirect(reverse('login'))
