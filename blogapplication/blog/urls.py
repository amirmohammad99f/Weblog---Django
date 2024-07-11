from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.post_list, name='posts_list'),
    path('posts/<int:id>', views.post_detail, name='posts_detail'),
]