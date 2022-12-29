from django import forms
from .models import Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UsernameField

"""
    comment - feedback of the user
    email - the email of the user
"""

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", )
        field_classes = {'username': UsernameField}
        
# class CommentForm(forms.Form):

#     comment = forms.CharField(max_length=300)
#     email = forms.EmailField()