from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    comment = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows':'1',
            'placeholder':'Say Something'
        })
    )
    class Meta:
        model = Comment
        fields = ['comment']