from django.urls import path
from .views import article_detail_view,add_article_view


app_name='article'

urlpatterns=[
    path('detail/<id>',article_detail_view, name='article_detail'),
    path('add_article',add_article_view, name='add_article'),
]