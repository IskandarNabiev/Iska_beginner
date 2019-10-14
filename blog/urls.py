from django.urls import path

# from .views import hello
# from .views import posts_list
# from .views import post_detail
# from .views import tags_list

from .views import *

urlpatterns = [
    path('', posts_list, name = 'posts_list_url'),
    path('post/<str:slug>/', post_detail, name = 'post_detail_url'),
    path('tags/', tags_list, name = 'tag_list_url'),
    path('tag/<str:slug>/', tag_detail, name = 'tag_detail_url')
]
