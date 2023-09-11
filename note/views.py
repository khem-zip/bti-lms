from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .forms import NoteForm
from django.contrib import messages
from .models import Note


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




def usernote_view(request):
    user =request.user
    notes = Note.objects.filter(uploader=user)
    return render(request,'note/usernote.html',{'notes':notes})

def updatenote_view(request,id):
    note =Note.objects.get(id=id)
    form = NoteForm(user=request.user, instance=note)
    if request.method == "POST":
        form = NoteForm(request.POST, request.FILES, user=request.user, instance=note)
        if form.is_valid():
            fm = form.save(commit=False)
            fm.uploader = request.user
            if not form.cleaned_data.get('file'):
                fm.file = note.file
            form.save()
            messages.success(request, 'Note successfully updated.')
        else:
            messages.error(request, 'Something went wrong.')

    context = {
        'form':form
    }
    return render(request,'note/updatenote.html', context)


def delete_note(request, id):
    # Retrieve the note object using get_object_or_404
    note = get_object_or_404(Note, id=id)
    user= request.user
    if note.uploader == user:
        note.delete()  # Delete the note object
        messages.success(request, 'Note successfully removed.')

        return redirect('note:allnote')  # Redirect to the list of notes or any other desired URL
    
    return HttpResponse('403 Not Authorized.')


