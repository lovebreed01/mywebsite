from dataclasses import fields
from django.forms import ModelForm
from django import forms
from .models import Post, Comment , MusicComment
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class PostCreateForm(ModelForm):
    body = forms.CharField(widget=SummernoteWidget())
    class Meta:
        model = Post
        exclude = ['author','slug']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ['author','post']

class MusicCommentForm(ModelForm):
    class Meta:
        model = MusicComment
        exclude = ['author','post']