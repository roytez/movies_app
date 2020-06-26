import math
from django.shortcuts import render
from django.core.paginator import Paginator

from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
# Create your views here.
from django.urls import resolve

from Movies.forms import MovieForm, GenreForm, DirectorForm, ActorForm, MusicForm
from Movies.models import Movie, Genre, Actor, Music, Director


def get_current_url_name(request):
    return resolve(request.path_info).url_name


def index_page(request):
    return render(request, 'index.html', {
        'current_route_name': get_current_url_name(request)
    })


def movie_list(request):
    # total_records_per_page = request.GET.get("total_records_per_page", 5)
    # page = request.GET.get("page", 1)
    #
    # if isinstance(page, str):
    #     try:
    #         page = int(page)
    #     except Exception as e:
    #         page = 1
    #
    movies = Movie.objects.filter(deleted=False)
    paginator = Paginator(movies, 3)
    page = request.GET.get('page')

    movies = paginator.get_page(page)

    # movies_count = movies.count()
    #
    # offset = 0
    #
    # if page > 1:
    #     offset = (page * total_records_per_page) - total_records_per_page
    #
    # movies = movies[offset:(total_records_per_page * page)]
    #
    # total_pages = math.ceil(movies_count / total_records_per_page)

    return render(request, 'movie/movie-list.html', {
        'current_route_name': get_current_url_name(request),
        'movies': movies,
        # 'pagination': {
        #     'total_pages': total_pages,
        #     'total_records': movies_count,
        #     'current_page': page,
        #     'next_page': page + 1,
        #     'has_next_page': page < total_pages,
        #     'page_range': range(1, (total_pages + 1))
        # }
    })


def movie_delete(request, pk_movie):
    try:
        movie = Movie.objects.get(id=pk_movie)
    except Exception as e:
        movie = None

    if movie is not None:
        movie.deleted = True
        movie.save()

    return HttpResponseRedirect('/movies/')


def movie_edit(request, pk_movie):
    try:
        movie = Movie.objects.get(id=pk_movie, deleted=False)
    except Exception as e:
        movie = None

    if movie is None:
        return HttpResponseNotFound()

    if request.method == "POST":
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/movies/")
    else:
        form = MovieForm(instance=movie)

    return render(request, 'movie/movie-edit.html', {
        'form': form,
        'movie': movie,
        'current_route_name': get_current_url_name(request)
    })


def movie_add(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/movies/')
    else:
        form = MovieForm()
    return render(request, 'movie/movie-add.html', {
        'form': form,
        'current_route_name': get_current_url_name(request)
    })


def genre_list(request):
    # total_records_per_page = request.GET.get("total_records_per_page", 5)
    # page = request.GET.get("page", 1)
    #
    # if isinstance(page, str):
    #     try:
    #         page = int(page)
    #     except Exception as e:
    #         page = 1

    genres = Genre.objects.filter(deleted=False)
    # genres_count = genres.count()
    #
    # offset = 0
    #
    # if page > 1:
    #     offset = (page * total_records_per_page) - total_records_per_page
    #
    # genres = genres[offset:(total_records_per_page * page)]
    #
    # total_pages = math.ceil(genres_count / total_records_per_page)

    paginator = Paginator(genres, 5)
    page = request.GET.get('page')
    genres = paginator.get_page(page)

    return render(request, 'genre/genre-list.html', {
        'current_route_name': get_current_url_name(request),
        'genres': genres,
        'items': genres
        # 'pagination': {
        #     'total_pages': total_pages,
        #     'total_records': genres_count,
        #     'current_page': page,
        #     'next_page': page + 1,
        #     'has_next_page': page < total_pages,
        #     'page_range': range(1, (total_pages + 1))
        # }
    })


def genre_add(request):
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/genre/')
    else:
        form = GenreForm()
    return render(request, 'genre/genre-add.html', {
        'form': form,
        'current_route_name': get_current_url_name(request)
    })


def genre_delete(request, pk_genre):
    try:
        genre = Genre.objects.get(id=pk_genre)
    except Exception as e:
        genre = None

    if genre is not None:
        genre.deleted = True
        genre.save()

    return HttpResponseRedirect('/genre/')


def genre_edit(request, pk_genre):
    try:
        genre = Genre.objects.get(id=pk_genre, deleted=False)
    except Exception as e:
        genre = None

    if genre is None:
        return HttpResponseNotFound()

    if request.method == "POST":
        form = GenreForm(request.POST, instance=genre)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/genre/")
    else:
        form = GenreForm(instance=genre)

    return render(request, 'genre/genre-edit.html', {
        'form': form,
        'genre': genre,
        'current_route_name': get_current_url_name(request)
    })


def director_list(request):
    total_records_per_page = request.GET.get("total_records_per_page", 5)
    page = request.GET.get("page", 1)

    if isinstance(page, str):
        try:
            page = int(page)
        except Exception as e:
            page = 1

    directors = Director.objects.filter(deleted=False)
    directors_count = directors.count()

    offset = 0

    if page > 1:
        offset = (page * total_records_per_page) - total_records_per_page

    directors = directors[offset:(total_records_per_page * page)]

    total_pages = math.ceil(directors_count / total_records_per_page)

    return render(request, 'director/director-list.html', {
        'current_route_name': get_current_url_name(request),
        'directors': directors,
        'pagination': {
            'total_pages': total_pages,
            'total_records': directors_count,
            'current_page': page,
            'next_page': page + 1,
            'has_next_page': page < total_pages,
            'page_range': range(1, (total_pages + 1))
        }
    })


def director_add(request):
    if request.method == 'POST':
        form = DirectorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/director/')
    else:
        form = DirectorForm()
    return render(request, 'director/director-add.html', {
        'form': form,
        'current_route_name': get_current_url_name(request)
    })


def director_delete(request, pk_director):
    try:
        director = Director.objects.get(id=pk_director)
    except Exception as e:
        director = None

    if director is not None:
        director.deleted = True
        director.save()

    return HttpResponseRedirect('/director/')


def director_edit(request, pk_director):
    try:
        director = Director.objects.get(id=pk_director, deleted=False)
    except Exception as e:
        director = None

    if director is None:
        return HttpResponseNotFound()

    if request.method == "POST":
        form = DirectorForm(request.POST, instance=director)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/director/")
    else:
        form = DirectorForm(instance=director)

    return render(request, 'director/director-edit.html', {
        'form': form,
        'director': director,
        'current_route_name': get_current_url_name(request)
    })


def actor_list(request):
    total_records_per_page = request.GET.get("total_records_per_page", 2)
    page = request.GET.get("page", 1)

    if isinstance(page, str):
        try:
            page = int(page)
        except Exception as e:
            page = 1

    actors = Actor.objects.filter(deleted=False)
    actors_count = actors.count()

    offset = 0

    if page > 1:
        offset = (page * total_records_per_page) - total_records_per_page

    actors = actors[offset:(total_records_per_page * page)]

    total_pages = math.ceil(actors_count / total_records_per_page)

    return render(request, 'actor/actor-list.html', {
        'current_route_name': get_current_url_name(request),
        'actors': actors,
        'pagination': {
            'total_pages': total_pages,
            'total_records': actors_count,
            'current_page': page,
            'next_page': page + 1,
            'has_next_page': page < total_pages,
            'page_range': range(1, (total_pages + 1))
        }
    })


def actor_add(request):
    if request.method == 'POST':
        form = ActorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/actor')
    else:
        form = ActorForm()
    return render(request, 'actor/actor-add.html', {
        'form': form,
        'current_route_name': get_current_url_name(request)
    })


def actor_delete(request, pk_actor):
    try:
        actor = Actor.objects.get(id=pk_actor)
    except Exception as e:
        actor = None

    if actor is not None:
        actor.deleted = True
        actor.save()

    return HttpResponseRedirect('/actor/')


def actor_edit(request, pk_actor):
    try:
        actor = Actor.objects.get(id=pk_actor, deleted=False)
    except Exception as e:
        actor = None

    if actor is None:
        return HttpResponseNotFound()

    if request.method == "POST":
        form = ActorForm(request.POST, instance=actor)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/actor/")
    else:
        form = ActorForm(instance=actor)

    return render(request, 'actor/actor-edit.html', {
        'form': form,
        'actor': actor,
        'current_route_name': get_current_url_name(request)
    })


def music_list(request):
    total_records_per_page = request.GET.get("total_records_per_page", 5)
    page = request.GET.get("page", 1)
    if isinstance(page, str):
        try:
            page = int(page)
        except Exception as e:
            page = 1

    tracks = Music.objects.filter(deleted=False)
    tracks_count = tracks.count()

    offset = 0

    if page > 1:
        offset = (page * total_records_per_page) - total_records_per_page

    tracks = tracks[offset:(total_records_per_page * page)]

    total_pages = math.ceil(tracks_count / total_records_per_page)

    return render(request, 'music/music-list.html', {
        'current_route_name': get_current_url_name(request),
        'tracks': tracks,
        'pagination': {
            'total_pages': total_pages,
            'total_records': tracks_count,
            'current_page': page,
            'next_page': page + 1,
            'has_next_page': page < total_pages,
            'page_range': range(1, (total_pages + 1))
        }
    })


def music_add(request):
    if request.method == 'POST':
        form = MusicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/music')
    else:
        form = MusicForm()
    return render(request, 'music/music-add.html', {
        'form': form,
        'current_route_name': get_current_url_name(request)
    })


def music_delete(request, pk_music):
    try:
        track = Music.ogjects.get(id=pk_music)
    except Exception as e:
        track = None

    if track is not None:
        track.deleted = True
        track.save()

    return HttpResponseRedirect('/music/')


def music_edit(request, pk_music):
    try:
        track = Music.objects.get(id=pk_music, deleted=False)
    except Exception as e:
        track = None

    if track is None:
        return HttpResponseNotFound()

    if request.method == "POST":
        form = MusicForm(request.POST, instance=track)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/music/")
    else:
        form = MusicForm(instance=track)

    return render(request, 'music/music-edit.html', {
        'form': form,
        'track': track,
        'current_route_name': get_current_url_name(request)
    })
