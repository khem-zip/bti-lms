from django.urls import path
from .views import allnotice_view


app_name='notice'

urlpatterns=[
    path('allnotice/',allnotice_view, name='allnotice')
]