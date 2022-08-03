from django.urls import path
from . import views

urlpatterns = [
    path('createpost', views.create_post, name='create_post'),
    path('getpost', views.get_post, name='get_post'),
    path('getpost/<int:id>', views.get_single_post, name='get_single_post'),
    path('deletepost/<int:id>', views.delete_post, name='delete_post'),
]
