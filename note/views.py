from django.shortcuts import render
from .forms import NoteForm
from django.contrib import messages


def addnote_view(request):
    form = NoteForm(user=request.user)
    if request.method == "POST":
        form = NoteForm(request.POST, request.FILES, user=request.user )
        if form.is_valid():
            fm = form.save(commit=False)
            fm.uploader = request.user
            form.save()
            messages.success(request, 'Note successfully added.')
        else:
            messages.error(request, 'Something went wrong.')
    context = {
        'form':form
    }
    return render(request,'note/addnote.html', context)




def allnote_view(request):
    return render(request,'note/allnote.html')