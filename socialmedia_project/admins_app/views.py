from django.shortcuts import render,redirect
from profile_app.models import UserProfileInfo
from post_app.models import Post
from comment_app.models import Comment
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from login_register_app.auth import admin_only
from django.db.models import Q
from .filters import  UsersFilter
from django.contrib import messages
from comment_app.models import Comment
import os
from django.contrib.auth.forms import PasswordChangeForm
from django.db.models import Q


# Create your views here.


@login_required
@admin_only
def Admins_Homepage(request):
    profile = UserProfileInfo.objects.all().order_by('-id')
    post = Post.objects.all()
    profile_count = profile.count()
    post_count = post.count()
    comment = Comment.objects.all()
    comment_count = comment.count()
    users = User.objects.all()
    admins = users.filter(is_staff=1)
    user_count = users.filter(is_staff=0).count()
    admin_count = users.filter(is_staff=1).count()

    context ={
        
        'profile':profile,
        'profile_count':profile_count,
        'post_count':post_count,
        'comment_count':comment_count,
        'user_count':user_count,
        'admin_count':admin_count,
        'post':post,
        'admins':admins,
    }

    return render (request,'admins_app/admins_homepage.html',context)





#let you view the list of the user and search user with email or starting with a letter of email
@login_required
@admin_only
def get_users(request):
    users = User.objects.filter(is_staff=0).order_by('-id')
    search_user = request.GET
    users_filter = UsersFilter(search_user,queryset= users)
    users_final = users_filter.qs
 
    context = {
        'users': users_final,
        
        'users_filter':users_filter
    }
    return render(request, 'admins_app/get_users.html', context)


# this function will promote regular user to admin user
@login_required
@admin_only
def promote_user(request,user_id):
    user = User.objects.get(id=user_id)
    user.is_staff=True
    user.save()
    messages.add_message(request, messages.SUCCESS, 'User promoted to admin')
    return redirect('/admins/show_admin')

#the user will be deleted 
@login_required
@admin_only
def delete_user(request,user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    messages.add_message(request, messages.SUCCESS, '{} user has been Deleted Successfully'.format(user.username))
    return redirect('/admins/show_user')

@login_required
@admin_only
def delete_admin(request,user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    messages.add_message(request, messages.SUCCESS, '{} Admin has been Deleted Successfully'.format(user.username))
    return redirect('/admins/show_admin')


#view all the amdins
@login_required
@admin_only
def get_admins(request):
    admins = User.objects.exclude(Q(is_staff=0) | Q( username= request.user)).order_by('-id')
    search_admin = request.GET
    admins_filter = UsersFilter(search_admin,queryset= admins)
    admins_final = admins_filter.qs

    context = {
        'admins': admins_final,
        
        'admins_filter':admins_filter
    }
    return render(request, 'admins_app/get_admin.html', context)

#demote user to the admin
@login_required
@admin_only
def demote_admin(request,user_id):
    user = User.objects.get(id=user_id)
    user.is_staff=False
    user.save()
    messages.add_message(request, messages.SUCCESS, 'Admin demoted to user')
    return redirect('/admins/show_user')




# login user can search other user profile by searching with their username 
# recommend profile are aso shown even if you don't now the full username starting with the letter you searched
@login_required
@admin_only
def get_profile(request):
    search_input = request.GET.get('q') or ''
    search_list = UserProfileInfo.objects.filter(Q(user__username__startswith=search_input))
    return render(request,'admins_app/get_profile.html',{'search_list':search_list})

#only admin will be able to delete the users profile
@login_required
@admin_only
def delete_profile(request,profile_id):
    user = UserProfileInfo.objects.get(id=profile_id)
    os.remove(user.profile_pic.path)
    user.delete()
    messages.add_message(request, messages.SUCCESS, '{} Profile has been Deleted Successfully'.format(user.user))
    return redirect('/admins/show_profile')

# admin can view all the user post and search post for certain user
@login_required
@admin_only
def get_post(request):
    search_input = request.GET.get('q') or ''
    post_list = Post.objects.filter(Q(author__username__startswith=search_input))
    return render(request,'admins_app/get_post.html',{'post_list':post_list})

#only admin will be able to delete the users post
@login_required
@admin_only
def delete_post(request,post_id):
    user_post = Post.objects.get(id=post_id)
  
    user_post.delete()
    messages.add_message(request, messages.SUCCESS, '{} user Post been Deleted Successfully'.format(user_post.author.username))
    return redirect('/admins/show_post')


# admin can view all the user post and search post for certain user
@login_required
@admin_only
def get_comment(request):
    search_input = request.GET.get('q') or ''
    comment_list = Comment.objects.filter(Q(author__username__startswith=search_input))
    return render(request,'admins_app/get_comment.html',{'comment_list':comment_list})

#only admin will be able to delete the users post
@login_required
@admin_only
def delete_comment(request,comment_id):
    user_comment = Comment.objects.get(id=comment_id)
    user_comment.delete()
    messages.add_message(request, messages.SUCCESS, '{} user Post been Deleted Successfully'.format(user_comment.author.username))
    return redirect('/admins/show_comment')


def AdminEditPassword(request):
    password_form = PasswordChangeForm(user = request.user)
    context = {'password_form':password_form,}

    if request.method == 'POST':
 
        password_form = PasswordChangeForm(data =request.POST,user = request.user)

        if password_form.is_valid() :    
            user = password_form.save()
            user.save()
            
            return redirect('/')
        
        else:
            messages.add_message(request, messages.ERROR, 'Something went wrong')
            return render(request,'admins_app/edit_admin_password.html',context) 
          

    else:
        return render(request,'admins_app/edit_admin_password.html',context)  
