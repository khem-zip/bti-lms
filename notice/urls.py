from django.urls import path
from .views import addnotice_view,allnotice_view


app_name='notice'

urlpatterns=[
    path('addnotice/',addnotice_view, name='addnotice'),
    path('allnotice/',allnotice_view, name='allnotice')
]