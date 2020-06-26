from Movies.models import Movie, Genre, Director, Actor, Music
from MoviesApp.forms import AppBaseForm
import django.forms as forms


class MovieForm(AppBaseForm):
    class Meta:
        model = Movie
        fields = ['title', 'year', 'runtime', 'description']


class GenreForm(AppBaseForm):
    class Meta:
        model = Genre
        fields = ['name']


class DirectorForm(AppBaseForm):
    class Meta:
        model = Director
        fields = ['name', 'about']


class ActorForm(AppBaseForm):
    class Meta:
        model = Actor
        fields = ['name', 'about']


class MusicForm(AppBaseForm):

    artist = forms.CharField(required=False)

    class Meta:
        model = Music
        fields = ['title', 'artist', 'composer']
