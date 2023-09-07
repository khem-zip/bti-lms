from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout as user_logout
from django.contrib import messages


def login_view(request):
    if request.method == 'GET':
        return render(request,'userauth/login.html')
    elif request.method == "POST":
        un = request.POST.get('username')
        pw = request.POST.get('password')
        user = authenticate(request,username = un,password=pw)
        if user is not None:
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