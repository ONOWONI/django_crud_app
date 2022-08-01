from urllib import request
import django
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
from django.shortcuts import render

# Create your views here.
def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.info(request, 'Email Taken')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
                    user.save();
                    print('user created')
                    return redirect('login')
        else:
            messages.info(request, 'Password does not match')
            return redirect('register')
        # return redirect('/')
    return render(request, 'reg.html')



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user:
            auth.login(request, user)
            messages.info(request, 'Access Granted')
            return redirect('/')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')



def logout(request):
    auth.logout(request)
    return redirect('/')