from django.shortcuts import render, HttpResponseRedirect
from .forms import LoginForm, UserSignUpForm
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from .models import Post
from .forms import PostFrom
from django.contrib.auth.models import Group
# Create your views here.
def home(request):
  post = Post.objects.all()
  return render(request,'blog/home.html',{'post':post})

def about(request):
 return render(request,'blog/about.html')

def contact(request):
 return render(request,'blog/contact.html')

def dashboard(request):
  if request.user.is_authenticated:
    post = Post.objects.all()
    user = request.user
    fname=user.get_full_name()
    gps = user.groups.all()
    return render(request,'blog/dashboard.html',{'posts':post,'full_name':fname,'groups':gps})
  else:
    return HttpResponseRedirect('/login/')

def user_logout(request):
 logout(request)
 return HttpResponseRedirect('/')

def user_login(request):
 if request.user.is_authenticated:
  return HttpResponseRedirect('/dashboard/')
 else:
  if request.method == 'POST':
   fm = LoginForm(request=request,data=request.POST)
   if fm.is_valid():
    uname = fm.cleaned_data['username']
    upassword = fm.cleaned_data['password']
    user=authenticate(username=uname,password=upassword)
    if user is not None:
     login(request,user)
     messages.success(request,'Logged in Successfully!')
     return HttpResponseRedirect('/dashboard/')
  else:
   fm = LoginForm()
  return render(request,'blog/login.html',{'fm':fm})

def user_signup(request):
 if request.method == 'POST':
  fm = UserSignUpForm(request.POST)
  if fm.is_valid():
   messages.success(request,'You are author now. You can post.')
   user = fm.save()
   group = Group.objects.get(name='auther')
   user.groups.add(group)
 else:
  fm = UserSignUpForm()
 return render(request,'blog/signup.html',{'fm':fm})


def addpost(request):
  if request.user.is_authenticated:
    if request.method == 'POST':
      fm = PostFrom(request.POST)
      if fm.is_valid():
        fm.save()
      fm = PostFrom()
    else:
      fm= PostFrom()  
    return render(request,'blog/addpost.html',{'form':fm})
  else:
    return HttpResponseRedirect('/login/')
def updatepost(request,id):
  if request.user.is_authenticated:
    if request.method == 'POST':
      data = Post.objects.get(pk=id)
      fm = PostFrom(request.POST,instance=data)
      if fm.is_valid():
        fm.save()
    else:
      data = Post.objects.get(pk=id)
      fm = PostFrom(instance=data)
    return render(request,'blog/updatepost.html',{'form':fm})
  else:
    return HttpResponseRedirect('/login/')

def deletepost(request,id):
  if request.user.is_authenticated:
    data = Post(pk=id)
    data.delete()
    return HttpResponseRedirect('/dashboard/')
  else:
    return HttpResponseRedirect('/login/')