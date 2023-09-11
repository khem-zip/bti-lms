from django.urls import path
from .views import addnote_view,usernote_view, updatenote_view, delete_note


app_name='note'

urlpatterns=[
    path('addnote/',addnote_view, name='addnote'),
    path('allnote/',usernote_view, name='allnote'),
    path('update/<id>',updatenote_view, name='update'),
    path('delete/<id>',delete_note, name='delete_note')
]