from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    post_image=models.ImageField(upload_to="images",null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    likes=models.ManyToManyField(User,related_name="post_like")

    def __str__(self):
        return self.title
    @property
    def like_count(self):
        return self.likes.all().count()
    
    @property
    def post_comment(self):
        return Comments.objects.filter(post=self)
    
class UserProfile(models.Model):
    profile_pic=models.ImageField(upload_to="images",null=True)
    bio=models.CharField(max_length=350)
    time_line_pic=models.ImageField(upload_to="images",null=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")

class Comments(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    comment=models.CharField(max_length=300)
    created_date=models.DateTimeField(auto_now_add=True)
    like=models.ManyToManyField(User,related_name="likes")
    active_status=models.BooleanField(default=True)

    def __str__(self):
        return self.post

    @property
    def like_count(self):
        return self.like.all().count()