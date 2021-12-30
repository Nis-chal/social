from django.shortcuts import render,redirect
from .models import UserProfileInfo
from post_app.models import Post
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from .forms import UserProfileInfoForm
from django.contrib import messages
from comment_app.models import Comment
from django.http import JsonResponse
from login_register_app.auth import user_only
# Create your views here.
@login_required
@user_only
def User_Profile(request,profile_id):
    profile = UserProfileInfo.objects.get(id = profile_id)
    user = profile.user
    posts = Post.objects.filter(author= user).order_by('-created_on')
    followers = profile.followers.all()
    if len(followers) == 0:
            is_following = False

    for follower in followers:
        if follower == request.user:
            is_following = True
            break  
        else:
            is_following = False 

    context = {
        'user':user,
        'profile':profile,
        'posts':posts,
        'is_following': is_following,
        'profile_active':'is-active'
        }
    return render (request,'profile_app/profile.html',context)

# login user can search other user profile by searching with their username 
# recommend profile are aso shown even if you don't now the full username starting with the letter you searched
@login_required
@user_only
def UserSearch(request):
    search_input = request.GET.get('q') or ''
    search_list = UserProfileInfo.objects.filter(Q(user__username__startswith=search_input))
    return render(request,'profile_app/profile_search.html',{'search_list':search_list})


@login_required
@user_only
def ProfileEdit(request,profile_id):
    user_profile = UserProfileInfo.objects.get(id = profile_id)
    profile_form = UserProfileInfoForm(instance=user_profile)

    context = {'profile_form':profile_form,'user_profile':user_profile}
        
    if request.method == 'POST':
        profile_form = UserProfileInfoForm(request.POST,request.FILES,instance=user_profile)


        if  profile_form.is_valid():
            
            profile_form.save()
                       
            
            return redirect('/profile/profile_page/{}'.format(user_profile.id))
        
        else:
            messages.add_message(request, messages.ERROR, 'Something went wrong')
            return render(request,'profile_app/profile_edit.html',context) 
          

    else:
        return render(request,'profile_app/profile_edit.html',context)    

@login_required
@user_only
def EditPassword(request):
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
            return render(request,'profile_app/change_password.html',context) 
          

    else:
        return render(request,'profile_app/change_password.html',context)  



#when user click follow to follow other user  the user will be added as follower for other user and 
#the other user will be added as a following of the user
#if not following 
@login_required
@user_only
def AddFollowers(request,profile_id):
    logged_in_user = request.user.profile.id
    profile = UserProfileInfo.objects.get(id = profile_id)
    user_profile = UserProfileInfo.objects.get(id = logged_in_user)
    user_id = profile.user
    user_profile_id = user_profile.user
    profile.followers.add(user_profile_id)
    user_profile.following.add(user_id)
    return redirect('/profile/profile_page/{}'.format(profile.id))

#when user click un-follow to un-follow other user  the user will be remove and no longer be follower  
#the other user will be removed  and won't be following the other user
#if is following 
@login_required
@user_only
def RemoveFollowers(request,profile_id):
    logged_in_user = request.user.profile.id
    profile = UserProfileInfo.objects.get(id = profile_id)
    user_profile = UserProfileInfo.objects.get(id = logged_in_user)
    user_id = profile.user
    user_profile_id = user_profile.user
    profile.followers.remove(user_profile_id)
    user_profile.following.remove(user_id)
    return redirect('/profile/profile_page/{}'.format(profile.id))


#user can be his activity log 
@login_required
@user_only
def Activity(request):
    logged_in_user = request.user
    post = Post.objects.filter(likes = logged_in_user).order_by('-created_on')
    comment = Comment.objects.filter(author = logged_in_user).order_by('-created_on')
    return render(request,'profile_app/activity.html',{'post':post,'comment':comment,'Activity_active':'is-active'})


#user will be able to see list of user which the user is  following
@login_required
@user_only
def Profile_Following_list(request,profile_id):
    profile = UserProfileInfo.objects.get(id = profile_id)
    user_profile = UserProfileInfo.objects.filter()
    user = profile.user
    followings=profile.following.all()
    context = {
        'user':user,
        'profile':profile,
        'user_profiles':user_profile,
        'followings':followings,

    } 
    return render (request,'profile_app/following_list.html',context)


#login_user will be able to follow and un_follow users
@login_required
@user_only
def togglefollowing(request,following_id):
    logged_in_user = request.user.profile.id
    
    profile = UserProfileInfo.objects.get(id = logged_in_user)
    user_profile = UserProfileInfo.objects.get(id = following_id)
    user_id = user_profile.user
    profile_id = profile.user
    followings = profile.following.all()
    is_remove = False
    
    if request.method == 'POST':
        for following in followings:
            if following == user_id:
                is_remove = True
                break
        if not is_remove:
            profile.following.add(user_id)
            user_profile.followers.add(profile_id)

        if is_remove:
            profile.following.remove(user_id)
            user_profile.followers.remove(profile_id)

        return JsonResponse({"is_remove":is_remove})


#login user can view user who are following the login user
@login_required
@user_only
def Profile_Follower_List(request,profile_id):
    profile = UserProfileInfo.objects.get(id = profile_id)
    user_profile = UserProfileInfo.objects.filter()
    user = profile.user
    followers=profile.followers.all()
    context = {
        'user':user,
        'profile':profile,
        'user_profiles':user_profile,
        'followers':followers,

    } 
    return render (request,'profile_app/follower_list.html',context)


#login user can remove the follower for follower list
@login_required
@user_only
def Delete_Follower(request,follower_id):
    logged_in_user = request.user.profile.id
    profile = UserProfileInfo.objects.get(id = logged_in_user)
    user_profile = UserProfileInfo.objects.get(id = follower_id)
    user_id = user_profile.user
    profile_id = profile.user
    followers = profile.followers.all()
    user_id = user_profile.user
    is_remove = False
    
    if request.method == 'POST':
        for follower in followers:
        
            if follower == profile_id:
                is_remove = True
                break

        if not is_remove:
            profile.followers.remove(user_id)
            user_profile.following.remove(profile_id)
            
        return JsonResponse({"is_remove":is_remove})
     