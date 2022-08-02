from django.urls import path
from . import views

urlpatterns = [
    path('create_post', views.create_post, name='create_post'),
    path('getpost', views.get_post, name='get_post'),
]
