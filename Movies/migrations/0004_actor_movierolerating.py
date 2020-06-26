# Generated by Django 2.2.5 on 2020-05-08 06:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Movies', '0003_director_moviehasdirector'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('about', models.TextField(default=None, null=True)),
                ('deleted', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'actor',
            },
        ),
        migrations.CreateModel(
            name='MovieRoleRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.PositiveIntegerField(max_length=2)),
                ('film_role', models.CharField(default=None, max_length=255, null=True)),
                ('deleted', models.BooleanField(default=False)),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Movies.Actor')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Movies.Movie')),
            ],
            options={
                'db_table': 'movie_role_rating',
            },
        ),
    ]