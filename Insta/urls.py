from django.contrib import admin
from django.urls import include, path
from Insta.views import HelloWorld, PostsView, PostDeleteView, PostUpdateView, PostDetailView, PostCreateView
urlpatterns = [
    path('', HelloWorld.as_view(), name = 'home'),
    path('posts/', PostsView.as_view(), name = 'posts'),
    path('post/<int:pk>', PostDetailView.as_view(), name = 'post_detail'),
    path('post/new/', PostCreateView.as_view(), name = 'make_post'),
    path('post/delete/<int:pk>', PostDeleteView.as_view(), name = 'post_delete'),
    path('post/update/<int:pk>', PostUpdateView.as_view(), name = 'post_update'),
]
