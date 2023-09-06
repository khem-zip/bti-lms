from django.urls import path
from .views import login_view,howto_view

app_name='userauth'

urlpatterns=[
    path('',login_view,name='login'),
    path('how_to_use',howto_view,name='howtouse')
]