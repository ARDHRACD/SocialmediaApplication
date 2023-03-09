from django.urls import path
from mediaweb import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path("register",views.SignUpView.as_view(),name="signup"),
    path("",views.SignInView.as_view(),name="signin"),
    path("home",views.IndexView.as_view(),name="index"),
    path("posts/<int:id>/comment/add",views.AddCommentView.as_view(),name="add-comment"),
    path("comments/<int:id>/like/add",views.LikeView.as_view(),name="like"),
    path("profiles/add",views.UserProfileCreateView.as_view(),name="profile-add"),
    path("profiles/details/add",views.ProfileDetailView.as_view(),name="profile-detail"),
    path("profile/<int:id>/change",views.ProfileUpdateView.as_view(),name="profile-change"),
    path("profile/posts/<int:id>/remove",views.PostRemoveView.as_view(),name="post-remove"),
    path("signout",views.SignOutView.as_view(),name="signout"),
    path("comments/<int:id>/like/remove",views.DislikeView.as_view(),name="dis-like"),
    path("comments/<int:id>/remove",views.CommentRemove.as_view(),name="remove-comment"),
    path("posts/<int:id>/like/add",views.PostlikeView.as_view(),name="post-like"),
    path("posts/<int:id>/like/remove",views.PostDislikeView.as_view(),name="post-dislike"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)