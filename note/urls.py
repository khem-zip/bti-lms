from django.urls import path
from .views import note_view


app_name='note'

urlpatterns=[
    path('',note_view,name='note')
]