from django.shortcuts import render

# Create your views here.
def login_view(request):
    return render(request,'userauth/login.html')
def howto_view(request):
    return render(request,'userauth/howto.html')