from django.urls import path
from .views import login_view,howto_view, profile_view,logout_view

app_name='userauth'

urlpatterns=[
    path('',login_view,name='login'),
    path('how_to_use',howto_view,name='howtouse'),
    path('profile',profile_view,name='profile'),
    path('logout',logout_view,name='logout'),
]