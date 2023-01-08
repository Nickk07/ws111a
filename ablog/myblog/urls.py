from django.urls import path
#from . import views
from .views import Home, ArticleDetails, AddPost, UpdatePost, DeletePost

urlpatterns = [
    #path('', views.home, name="home")
    path('', Home.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetails.as_view(), name='article-detail'),
    path('add_post/', AddPost.as_view(), name='add_post'),
    path('article/edit/<int:pk>', UpdatePost.as_view(), name='update_post'),
    path('article/<int:pk>/remove', DeletePost.as_view(), name='delete_post'),
]