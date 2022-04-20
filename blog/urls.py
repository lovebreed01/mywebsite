from unicodedata import name
from django.urls import path
from .views import (
    delete_post,
    home, 
    create_post,
    detail,
    edit_post,
    delete_post,
    music_page,
    musics,
    news,
    trending
     )
urlpatterns = [
    path('', home, name='home' ),
    path('post/<slug>/', detail, name='detail' ),
    path('music/<slug>/', music_page, name='music' ),
    path('songs/', musics , name='songs' ),
    path('news/', news , name='news' ),
    path('trending/', trending , name='trending' ),
    path('create/' , create_post, name='create' ),
    path('post/<slug>/edit/', edit_post, name='edit'),
    path('post/<slug>/delete/', delete_post, name='delete')

]
