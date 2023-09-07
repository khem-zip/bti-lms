from django.shortcuts import render

# Create your views here.
def addnote_view(request):
    return render(request,'note/addnote.html')
def allnote_view(request):
    return render(request,'note/allnote.html')