from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def home(request):
    x = '!'
    return render(request, 'home.html', {'obj': x})


def register(request):
    if request.method == 'POST':
        username = request.POST["username"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        password = request.POST["password"]
        password1 = request.POST["password1"]
        if password == password1:
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, password=password)
            user.save();
            return redirect('login')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('register')
    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('appli')
        else:
            return redirect('login')
    return render(request, 'login.html')


def appli(request):
    if request.method == 'POST':
        username = request.POST["username"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        password = request.POST["password"]
        password1 = request.POST["password1"]
        if password == password1:
            user = User.objects.create_user(username=username, first_name=first_name,last_name=last_name, password=password)
            user.save();
            messages.info(request, 'user created')
            return redirect('appli')
        else:
            return redirect('login')
    return render(request, 'appli.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
