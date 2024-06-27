from django.urls import path
from . import views
urlpatterns = [
    path('', views.PostListView, name="post list"),
    path('add/', views.PostAdd, name="post add"),
    path('count/<int:post_id>/', views.PostLikeAdd,name='count add'),
    path('delete/<int:post_id>/', views.PostDelete,name='post delete'),
    path('edit/<int:post_id>/', views.PostEdit,name='post edit'),
    #path('index/', views.index, name='index'),
]
