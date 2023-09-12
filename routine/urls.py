from django.urls import path
from .views import routine_view


app_name='routine'

urlpatterns=[
    path('',routine_view, name='routine')
]