from this import d
from tkinter import Widget
from django import forms
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect

from users.models import User
from project.models import Post, Comment


class PostCreateFrom(forms.ModelForm):
    

    def save(self, user: User, commit: bool = False):
        post = super().save(False) 


        post.user = user

        if commit:
            post.save()  

    class Meta:
        model = Post
        exclude = ["user"]

class PostModifyFrom(forms.ModelForm):

    class Meta:
        model = Post
        exclude = ["user"]
    
class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [ "post" ,"body"]
        Widget = {
            "post" : forms.HiddenInput
        }