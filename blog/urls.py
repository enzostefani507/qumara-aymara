from django.urls import path
from .views import PostList, PostDetail, tratar_favorito

urlpatterns = [
    path('', PostList.as_view(), name='posts'),
    path('/<int:pk>', PostDetail.as_view(),name='detalle_post'),
    path('/fav/<int:id>', tratar_favorito,name='tratar_favorito'),
]