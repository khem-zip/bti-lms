from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout as user_logout
from django.contrib import messages
from django.contrib.auth.models import User


def login_view(request):
    if request.method == 'GET':
        return render(request,'userauth/login.html')
    elif request.method == "POST":
        un = request.POST.get('username')
        pw = request.POST.get('password')
        user = authenticate(request,username = un,password=pw)
        if user is not None:
            print(user)
            us = User.objects.get(username = user)
            if us.is_superuser:
                login(request,user)
                return redirect('/admin')

            login(request,user)
            return redirect('userauth:profile')
        
        else:
            messages.error(request,'User not found.')
            print('Not registered')
            return render(request,'userauth/login.html')
    


def howto_view(request):
    return render(request,'userauth/howto.html')


def profile_view(request):
    return render(request, 'userauth/profile.html')


def logout_view(request):
    user_logout(request)
    messages.success(request,'Logged out successfully.')
    return redirect('userauth:login')