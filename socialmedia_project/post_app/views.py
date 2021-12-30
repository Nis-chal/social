from django.shortcuts import render,redirect
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post
from django.http import JsonResponse
from comment_app.forms import CommentForm
from comment_app.models import Comment
from login_register_app.auth import user_only
import os
from django.db.models import Q
# Create your views here.
@login_required
@user_only  
def Add_Post(request):
    #user must be logged in to add post
    #  an author field is automatically set to user while posting a posting 
    if  request.method =='POST':
        post_form = PostForm(request.POST,request.FILES)

        if post_form.is_valid():
            posted = post_form.save(commit=False)
            posted.author = request.user
            posted.save()
            return redirect('/post/post_list')
            
    else:
        post_form = PostForm()
    context = {
        
        'post_form':post_form,
        'post_active':'post_active'
        
    }
    return render(request,'post_app/add_post.html',context)

# followed user post will be shown 
@login_required
@user_only
def PostList(request):
    logged_in_user = request.user
    posts = Post.objects.filter(Q(author__profile__followers__in = [logged_in_user.id] ) | Q (author = request.user)).order_by('-created_on')

    context = {
        'post_list':posts,
        'postlist_active':'is-active'
        
    }
    return render(request,'post_app/post_list.html',context)

# when user like a ajax call is made using this function to get no of like in post and if the postis like or not
@login_required
@user_only
def AddLike(request,post_id):
    # an ajax call is made using this function
    post = Post.objects.get(id = post_id)
    like_count = post.likes.count()
    is_like = False
    if request.method =='POST':
        for like in post.likes.all():
            if like == request.user:
                is_like =True
                like_count = post.likes.count()
                break
        if not is_like:
            post.likes.add(request.user)
            like_count = post.likes.count()
                
            
        if is_like:
            post.likes.remove(request.user) 
            like_count = post.likes.count()

     

    return JsonResponse({"is_like":is_like,"like_count":like_count})

@login_required
@user_only
def PostEdit(request,post_id):
    post = Post.objects.get(id = post_id)
    # ti will determine which post to edit with the help of post_id 
    if request.user == post.author:
        if request.method == "POST":     
            if request.FILES.get('post_image'):
                # if you are going to replace your image it will replace and remove the previous one
                os.remove(post.post_image.path)
                post.description = request.POST['description']
                post.post_image= request.FILES['post_image']
                post.save()
                return redirect('/post/post_list')
            else:
                post.description = request.POST['description']
                post.save()       
                return redirect('/post/post_list')
        context = {
            'post':post,
            'activate_file':'active'
        }
        return render(request,'post_app/post_edit.html',context)
    
    else:
        return redirect('/404error')


@login_required
@user_only
def PostDelete(request,post_id):
    
    post = Post.objects.get(id = post_id)
    if request.user == post.author:
        os.remove(post.post_image.path)
        post.delete()
        return redirect('/post/post_list')
    else:
        return redirect('/404error')



# it will take you to a post-detail page were  you can comment on  post
@login_required
@user_only
def PostDetail(request,post_id):
    
    post = Post.objects.get(id = post_id)
    comment_form = CommentForm()
    comments = Comment.objects.filter(post = post).order_by('-created_on')
    context ={
        'post':post,
        'comment_form':comment_form,
        'comments':comments,
    }
    if request.method =='POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.author = request.user
            new_comment.post = post
            new_comment.save()
            return render(request,'post_app/post_detail.html',context)

    return render(request,'post_app/post_detail.html',context)