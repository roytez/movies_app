"""MoviesApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from Movies.views import index_page, movie_list, movie_add, genre_list, genre_add, director_list, director_add, \
    actor_list, actor_add, music_list, music_add, movie_delete, movie_edit, genre_delete, director_delete, actor_delete, \
    music_delete, genre_edit, director_edit, actor_edit, music_edit

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page, name="index_page"),
    path('movies/', movie_list, name='movie_list'),
    path('movies/add', movie_add, name='movie_add'),
    path('movies/<int:pk_movie>/delete', movie_delete, name='movie_delete'),
    path('movies/<int:pk_movie>/edit', movie_edit, name='movie_edit'),
    path('genre/', genre_list, name='genre_list'),
    path('genre/add', genre_add, name='genre_add'),
    path('genre/<int:pk_genre>/delete', genre_delete, name='genre_delete'),
    path('genre/<int:pk_genre>/edit', genre_edit, name='genre_edit'),
    path('director/', director_list, name='director_list'),
    path('director/add', director_add, name='director_add'),
    path('director/<int:pk_director>/delete', director_delete, name='director_delete'),
    path('director/<int:pk_director>/edit', director_edit, name='director_edit'),
    path('actor/', actor_list, name='actor_list'),
    path('actor/add', actor_add, name='actor_add'),
    path('actor/<int:pk_actor>/delete', actor_delete, name='actor_delete'),
    path('actor/<int:pk_actor>/edit', actor_edit, name='actor_edit'),
    path('music/', music_list, name='music_list'),
    path('music/add', music_add, name='music_add'),
    path('music/<int:pk_music>/delete', music_delete, name='music_delete'),
    path('music/<int:pk_music>/edit', music_edit, name='music_edit'),
]
