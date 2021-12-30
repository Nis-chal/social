from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from . models import Comment
from . forms import CommentForm


# Create your views here.

#a specific comment can be edit
@login_required
def CommentEdit(request,comment_id):

    comment = Comment.objects.get(id = comment_id)
    if request.user == comment.author:

        post_id = comment.post.id
        comment_form = CommentForm(instance=comment)
        # ti will determine which comment to edit with the help of comment_id 
        if request.method == "POST":
        
            comment_form = CommentForm(request.POST,instance=comment)
            if comment_form.is_valid():
                comment_form.save()
             
                return redirect('/post/post_detail/{}'.format(post_id))

            else:
                
                return redirect('/comment/comment_edit/{}'.format(comment_id))

        else:
            
        
            context = {
            'comment':comment,
            'comment_form':comment_form,
            'activate_file':'active'
            }
            return render(request,'comment_app/comment_edit.html',context)
    
    else:
        return redirect('/404error')

       

@login_required
def CommentDelete(request,comment_id):
    comment = Comment.objects.get(id = comment_id)
    if request.user == comment.author:

        post_id = comment.post.id
        comment.delete()
        return redirect('/post/post_detail/{}'.format(post_id))
    
    else:
        return redirect('/404error')