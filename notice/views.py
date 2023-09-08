from django.shortcuts import render

# Create your views here.
def addnotice_view(request):
    return render(request,'notice/addnotice.html')
def allnotice_view(request):
    return render(request,'notice/allnotice.html')