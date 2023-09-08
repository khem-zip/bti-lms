from django.urls import path
from .views import course_view, course_detail_view


app_name='course'

urlpatterns=[
    path('',course_view, name='course'),
    path('detail/<int:id>',course_detail_view, name='detail'),


]