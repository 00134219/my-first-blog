from django.urls import path
from . import views

app_name = 'post'  

urlpatterns = [
  path('', views.post_list, name='post_list'),
  path('post/<int:pk>/', views.post_detail, name='post_detail'),
  path('post/new/', views.post_new, name='post_new'),
  # 知識の技
  path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
  path('<int:pk>', views.PostDetail, name='detail'),  
  path('comment/create/<int:pk>/', views.CommentCreate.as_view(), name='comment_create'), 
  ]