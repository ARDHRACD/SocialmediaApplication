from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from mediaweb.models import Post,Comments,UserProfile

class RegistrationForm(UserCreationForm):

    class Meta:
        model=User
        fields=["username","email","password1","password2"]

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())

class PostForm(forms.ModelForm):

    class Meta:
        model=Post
        fields=["title","description","post_image"]

class UserProfileForm(forms.ModelForm):

    class Meta:
        model=UserProfile
        fields=["profile_pic","bio","time_line_pic"]