# Generated by Django 3.2 on 2023-03-01 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='filmwork',
            options={'ordering': ['id'], 'verbose_name': 'Кинопроизведение', 'verbose_name_plural': 'Кинопроизведения'},
        ),
        migrations.AddField(
            model_name='filmwork',
            name='persons',
            field=models.ManyToManyField(related_name='filmwork_persons', through='movies.PersonFilmwork', to='movies.Person'),
        ),
        migrations.AlterField(
            model_name='filmwork',
            name='creation_date',
            field=models.DateField(verbose_name='creation_date'),
        ),
        migrations.AlterField(
            model_name='filmwork',
            name='description',
            field=models.TextField(max_length=2048, verbose_name='filmwork_desc'),
        ),
        migrations.AlterField(
            model_name='filmwork',
            name='genres',
            field=models.ManyToManyField(related_name='genres', through='movies.GenreFilmwork', to='movies.Genre'),
        ),
        migrations.AlterField(
            model_name='filmwork',
            name='type',
            field=models.CharField(choices=[('movie', 'movie'), ('tv_show', 'tv_show')], default='movie', max_length=128, verbose_name='type'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='description',
            field=models.TextField(blank=True, default='Без описания', verbose_name='genre_desc'),
        ),
        migrations.AlterField(
            model_name='personfilmwork',
            name='role',
            field=models.CharField(choices=[('actor', 'Actor'), ('director', 'Director'), ('writer', 'Writer')], default='actor', max_length=35, null=True, verbose_name='role'),
        ),
        migrations.AddIndex(
            model_name='filmwork',
            index=models.Index(fields=['creation_date'], name='film_work_creation_date_idx'),
        ),
        migrations.AddIndex(
            model_name='genrefilmwork',
            index=models.Index(fields=['film_work', 'genre'], name='film_work_genre_idx'),
        ),
        migrations.AddConstraint(
            model_name='genrefilmwork',
            constraint=models.UniqueConstraint(fields=('film_work', 'genre'), name='film_work_genre'),
        ),
    ]
