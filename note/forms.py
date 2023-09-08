# import form class from django
from django import forms
from .models import Note
from course.models import Course

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['course','name','file']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Get the user from kwargs
        super(NoteForm, self).__init__(*args, **kwargs)
        
        if user:
            self.fields['course'].queryset = Course.objects.filter(teacher=user)

