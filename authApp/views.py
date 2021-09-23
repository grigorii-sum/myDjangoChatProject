from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .forms import CreateUserForm
from chatApp.models import Message


def register_page(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

    context = {
        'title': 'Регистрация',
        'form': form,
    }
    return render(request, 'authApp/register.html', context)


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            new_message = Message.create(author_id=user, text="---------- ПОЛЬЗОВАТЕЛЬ ЗАШЕЛ В ЧАТ ----------")
            new_message.save()

            return redirect('chat')

    context = {
        'title': 'Вход',
    }
    return render(request, 'authApp/login.html', context)


def logout_user(request):
    user = User.objects.get(id=request.user.id)
    logout(request)

    new_message = Message.create(author_id=user, text="---------- ПОЛЬЗОВАТЕЛЬ ВЫШЕЛ ИЗ ЧАТА ----------")
    new_message.save()

    return redirect('login')


