from os import name
from django.urls import path
from . import views

app_name ='post_app'
urlpatterns = [
    path('add_post',views.Add_Post,name='add_post'),
    path('post_list',views.PostList,name='post_list'),
    path('<int:post_id>/like',views.AddLike,name ='like'),
    path('post_edit/<int:post_id>',views.PostEdit,name ='edit'),
    path('post_delete/<int:post_id>',views.PostDelete,name ='post_delete'),
    path('post_detail/<int:post_id>',views.PostDetail,name='post_detail')
    
]