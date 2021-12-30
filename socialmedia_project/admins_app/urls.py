from django.urls import path
from . import views

urlpatterns = [
    path('admins',views.Admins_Homepage),

    path('show_user',views.get_users),
    path('promote_user/<int:user_id>',views.promote_user),
    path('delete_user/<int:user_id>',views.delete_user),

    path('show_admin',views.get_admins),
    path('demote_admin/<int:user_id>',views.demote_admin),
    path('delete_admin/<int:user_id>',views.delete_admin),

    path('show_profile',views.get_profile),
    path('delete_profile/<int:profile_id>',views.delete_profile),

    path('show_post',views.get_post),
    path('delete_post/<int:post_id>',views.delete_post),

    path('show_comment',views.get_comment),
    path('delete_comment/<int:comment_id>',views.delete_comment),

    path('change_password',views.AdminEditPassword),
    
]