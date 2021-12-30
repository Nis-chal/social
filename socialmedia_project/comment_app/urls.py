from django.urls import path
from . import views

urlpatterns = [
    path('comment_edit/<int:comment_id>',views.CommentEdit,name ='comment_edit'),
    path('comment_delete/<int:comment_id>',views.CommentDelete,name ='comment_delete'),
    
]