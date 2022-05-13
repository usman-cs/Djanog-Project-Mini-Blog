from .models import Post
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django import forms
from django.contrib.auth.models import User
class LoginForm(AuthenticationForm):
 username = UsernameField(widget=forms.TextInput(attrs={'class':'form-control','autofocus':True}))
 password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','autofocus':True}),label='Password ',strip=False)

class UserSignUpForm(UserCreationForm):
 password1 = forms.CharField(label='Password ',widget=forms.PasswordInput(attrs={'class':'form-control'}))
 password2 = forms.CharField(label='Enter Password Again ',widget=forms.PasswordInput(attrs={'class':'form-control'}))
 class Meta:
  model = User
  fields = ['username','first_name','last_name','email']
  labels = {'first_nanme':'First Names ','last_name':'Last Name ','username':'User Name ','email':'Email '}
  widgets = {'username':forms.TextInput(attrs={'class':'form-control'}),
  'email':forms.EmailInput(attrs={'class':'form-control'}),
  'first_name':forms.TextInput(attrs={'class':'form-control'}),
  'last_name':forms.TextInput(attrs={'class':'form-control'}),

  }


class PostFrom(forms.ModelForm):
 class Meta:
  model = Post
  fields = ['title','desc']
  labels = {'title':'Title ','desc':'Description '}
  widgets = {
   'title':forms.TextInput(attrs={'class':'form-control'}),
    'desc':forms.Textarea(attrs={'class':'form-control'}),
  }