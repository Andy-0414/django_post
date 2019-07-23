# from django.urls import path, include
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PostView,LoginView,UserView

post_list = PostView.as_view({
    'post': 'create',
    'get': 'list'
})
post_detail = PostView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = format_suffix_patterns([
    url('posts/', post_list, name='post_list'),
    url('posts/<int:pk>/', post_detail, name='post_detail'),
    url('auth/login/', LoginView.as_view(), name="login"),
    url("auth/user/", UserView.as_view(),name="user"),
])