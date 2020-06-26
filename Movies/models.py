from django.db import models


# Create your models here.
class MovieManager(models.Manager):
    def function(self):
        pass
        # self.queryset


class Movie(models.Model):
    title = models.CharField(max_length=255)  # rocky 3
    year = models.PositiveIntegerField()
    runtime = models.PositiveIntegerField(default=0, null=True)  # null=True ?
    rating = models.DecimalField(max_digits=2, decimal_places=2, default=0, null=True)
    description = models.TextField(default=None, null=True)
    votes = models.PositiveIntegerField(default=0, null=True)

    deleted = models.BooleanField(default=False)
    objects = MovieManager()

    class Meta:
        db_table = 'movie'
        app_label = 'Movies'


class MovieComment(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    movie = models.ForeignKey('Movies.Movie', on_delete=models.DO_NOTHING)

    parent = models.ForeignKey('self', default=None, null=True, on_delete=models.DO_NOTHING)
    # Ważne! w tym przypadku odpowiada za komentarze
    # odpowiedz na komentarz, który idzie w głąb przykład poniżej z id

    # ID = 1
    # ID = 2 PARENT = 1
    # ID = 3 PARENT = 2
    # ID = 4 PARENT = 1
    # ...

    # IP

    # 1
    #   2
    #   3
    #   4
    #     5
    #     6
    #   7

    # 6 IP = 1.4.6
    # SELECT * FROM comment LIKE ip '1.4%'

    # w przypadku on_delete istnieje opcja models.CASCADE
    # jeżeli ją ustawimy to po usunięciu filmu(rekordu z tabeli movie) automatycznie usunie nam wszystkie komentarze
    # powiązane z tym filmem

    deleted = models.BooleanField(default=False)  # True

    # select * from movie_comment where deleted = 0;
    class Meta:
        db_table = 'movie_comment'
        app_label = 'Movies'


class Genre(models.Model):
    name = models.CharField(max_length=255)

    deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'genre'
        app_label = 'Movies'

    # CamelCase
    # camel_case


class MovieGenre(models.Model):  # movies_has_genres
    movie = models.ForeignKey('Movies.Movie', on_delete=models.DO_NOTHING)
    genre = models.ForeignKey('Movies.Genre', on_delete=models.DO_NOTHING)

    deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'movie_genre'
        app_label = 'Movies'


class Director(models.Model):
    name = models.CharField(max_length=255)
    about = models.TextField(default=None, null=True)

    deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "director"
        app_label = "Movies"


class MovieDirector(models.Model):
    movie = models.ForeignKey('Movies.Movie', on_delete=models.DO_NOTHING)
    director = models.ForeignKey('Movies.Director', on_delete=models.DO_NOTHING)

    deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'movie_director'
        app_label = 'Movies'


class Actor(models.Model):  # dodać
    name = models.CharField(max_length=255)
    about = models.TextField(default=None, null=True)

    deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'actor'
        app_label = 'Movies'


class MovieRole(models.Model):
    level = models.PositiveIntegerField(default=0)
    film_role = models.CharField(max_length=255, default=None, null=True)
    level = models.PositiveIntegerField(default=0, null=True)
    movie = models.ForeignKey('Movies.Movie', on_delete=models.DO_NOTHING)
    actor = models.ForeignKey('Movies.Actor', on_delete=models.DO_NOTHING)

    deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'movie_role'
        app_label = 'Movies'


class RoleComment(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.DecimalField(max_digits=2, decimal_places=2, default=0, null=True)
    movie_role = models.ForeignKey('Movies.MovieRole', on_delete=models.DO_NOTHING)

    parent = models.ForeignKey('self', default=None, null=True, on_delete=models.DO_NOTHING)

    deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'role_comment'
        app_label = 'Movies'


class Music(models.Model):  # dodać
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255, null=True, default=None)
    composer = models.CharField(max_length=255, null=True, default=None)
    rating = models.DecimalField(max_digits=2, decimal_places=2, default=0, null=True)
    # movie = models.ForeignKey('Movies.Movie', on_delete=models.DO_NOTHING)

    deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'music'
        app_label = 'Movies'


class MovieMusic(models.Model):
    movie = models.ForeignKey('Movies.Movie', on_delete=models.DO_NOTHING)
    genre = models.ForeignKey('Movies.Genre', on_delete=models.DO_NOTHING)

    deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'movie_music'
        app_label = 'Movies'
