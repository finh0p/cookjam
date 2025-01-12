from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterUserForm


def index(request):
    return render(request,
                  'nutrition/index.html')


def account_page(request, id):
    authorized_user = None
    if request.user.is_authenticated:
        authorized_user = request.user
    user = get_object_or_404(User,
                             id=id)
    # Добавить проверку на то страница ли это самого авторизованного
    # пользователя или другого, чтобы использовать разные шаблоны для
    # своего аккаунта и аккаунта другого пользователя
    if authorized_user.id == user.id:
        return render(request,
                      'account/my_account_page.html',
                      {
                          'user': user,
                          'request': request
                      })
    else:
        return render(request,
                      'account/another_account_page.html',
                      {'user': user,
                       'request': request})


def registration(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            # получаем имя пользователя и пароль из формы
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            # выполняем аутентификацию
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'account/signup.html', {'form': form})


def log_in(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        login(request, user)
        return redirect('/')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/')


def add_meals(request):
    pass
