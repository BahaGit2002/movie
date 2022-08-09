# Generated by Django 4.0.3 on 2022-08-08 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_movie_actors_alter_movie_directors_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(blank=True, related_name='film_actor', to='main.actor', verbose_name='Актеры'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='directors',
            field=models.ManyToManyField(blank=True, related_name='film_director', to='main.actor', verbose_name='Режиссер'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(blank=True, to='main.genre', verbose_name='Жанры'),
        ),
    ]