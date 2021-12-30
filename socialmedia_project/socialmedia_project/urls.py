"""socialmedia_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from os import name
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from admins_app import urls
from post_app import urls
from comment_app import urls
from profile_app import urls
from login_register_app import urls
from django.conf.urls.static import static
from django.conf import settings
from login_register_app import views
from django.contrib.auth import views as auth_views

urlpatterns = [


    # five apps were included in urls
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('404error',views.Not_found,name ='404error'),
    path('account/',include('login_register_app.urls')),
    path('post/',include('post_app.urls')),
    path('comment/',include('comment_app.urls')),
    path('profile/',include('profile_app.urls')),
    path('admins/',include('admins_app.urls')),



   #four auth views were used to reset,sent-email,update-password,show success sign 
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name = 'login_register_app/password_reset.html'),name="reset_password"),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name = 'login_register_app/password_reset_done.html'), name ="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name ='login_register_app/password_reset_confirm.html'), name ="password_reset_confirm"),
    path('reset_password_complete/' ,auth_views.PasswordResetCompleteView.as_view(template_name ='login_register_app/password_reset_complete.html'), name="password_reset_complete"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
