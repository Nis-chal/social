from django import forms
from django.contrib.auth.models import User

from .models import Post

class PostForm(forms.ModelForm):
    description = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows':'3',
            'placeholder':'Say Something'
        })
    )
    class Meta:
        model = Post
        fields = ['post_image','description']
