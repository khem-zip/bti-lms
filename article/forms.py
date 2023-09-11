# import form class from django
from django import forms
from .models import Article
from course.models import Course
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        widgets = {
            'content': SummernoteWidget(),
            # 'bar': SummernoteInplaceWidget(),
        }
        fields = ['course','title','content','excerpt','img']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Get the user from kwargs
        super(ArticleForm, self).__init__(*args, **kwargs)
        
        if user:
            self.fields['course'].queryset = Course.objects.filter(teacher=user)

