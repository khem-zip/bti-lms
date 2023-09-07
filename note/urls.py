from django.urls import path
from .views import addnote_view,allnote_view


app_name='note'

urlpatterns=[
    path('addnote/',addnote_view, name='addnote'),
    path('allnote/',allnote_view, name='allnote')
]