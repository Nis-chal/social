from django.urls import path
from . import views

app_name = 'profile_app'
urlpatterns = [
    path('profile_page/<int:profile_id>',views.User_Profile,name='user_profile'),

    path('search_profile',views.UserSearch),

    path('profile_edit/<int:profile_id>',views.ProfileEdit,name='profile_edit'),


    path('follow_user/<int:profile_id>',views.AddFollowers,name ='follow'),
    path('unfollow_user/<int:profile_id>',views.RemoveFollowers,name='unfollow'),

    path('change_password',views.EditPassword),

    path('activity',views.Activity),


    
    path('following/<int:profile_id>',views.Profile_Following_list,name='following_list'),
    path('toggle_following/<int:following_id>',views.togglefollowing,name='toggle_following_user'),

    path('follower/<int:profile_id>',views.Profile_Follower_List,name='follower_list'),
    path('remove_follower/<int:follower_id>',views.Delete_Follower,name='Remove_following_user'),


]