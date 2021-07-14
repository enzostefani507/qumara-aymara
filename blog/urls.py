from django.conf.urls import url
from django.urls import path
from .views import PostList, PostDetail

urlpatterns = [
    path('', PostList.as_view(), name='posts'),
    path('/<int:pk>', PostDetail.as_view(),name='post_class')
]