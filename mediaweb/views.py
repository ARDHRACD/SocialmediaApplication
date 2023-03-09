from django.shortcuts import render,redirect
from mediaweb.forms import RegistrationForm,LoginForm,PostForm,UserProfileForm
from django.views.generic import View,CreateView,FormView,ListView,TemplateView,UpdateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from mediaweb.models import Post,UserProfile,Comments

class SignUpView(CreateView):
    model=User
    form_class=RegistrationForm
    template_name="register.html"
    success_url=reverse_lazy("signin")

class SignInView(FormView):
    template_name="login.html"
    form_class=LoginForm

    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                return redirect("index")
            else:
                return render(request,"login.html",{"form":self.form_class})
            
class SignOutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("signin")
            
class IndexView(CreateView,ListView):
    model=Post
    template_name="index.html"
    context_object_name="posts"
    form_class=PostForm
    success_url=reverse_lazy("index")

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    
    def get_queryset(self):
        return Post.objects.all().order_by("-date")
    
class AddCommentView(View):

    def post(self,request,*args,**kwargs):
        pid=kwargs.get("id")
        pos=Post.objects.get(id=pid)
        usr=request.user
        com=request.POST.get("comment")
        Comments.objects.create(user=usr,post=pos,comment=com)
        return redirect("index")
    
class LikeView(View):

    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        com=Comments.objects.get(id=id)
        com.like.add(request.user)
        com.save()
        return redirect("index")
    
class DislikeView(View):

    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        com=Comments.objects.get(id=id)
        com.like.remove(request.user)
        com.save()
        return redirect("index")
    
class UserProfileCreateView(CreateView):
    model=UserProfile
    form_class=UserProfileForm
    template_name="profile-add.html"
    success_url=reverse_lazy("index")

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    
class ProfileDetailView(TemplateView):
    template_name="profile-detail.html"

class ProfileUpdateView(UpdateView):
    model=UserProfile
    template_name="profile-update.html"
    form_class=UserProfileForm
    success_url=reverse_lazy("index")
    pk_url_kwarg="id"

class PostRemoveView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        Post.objects.get(id=id).delete()
        return redirect("index")
    
class CommentRemove(View):

    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        Comments.objects.get(id=id).delete()
        return redirect("index")
    
class PostlikeView(View):

    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        pos=Post.objects.get(id=id)
        pos.likes.add(request.user)
        pos.save()
        return redirect("index")
    
class PostDislikeView(View):

    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        pos=Post.objects.get(id=id)
        pos.likes.remove(request.user)
        pos.save()
        return redirect("index")