# Generated by Django 3.2 on 2023-03-01 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_alter_filmwork_persons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filmwork',
            name='genres',
            field=models.ManyToManyField(through='movies.GenreFilmwork', to='movies.Genre'),
        ),
        migrations.AlterField(
            model_name='filmwork',
            name='persons',
            field=models.ManyToManyField(through='movies.PersonFilmwork', to='movies.Person'),
        ),
        migrations.AlterField(
            model_name='personfilmwork',
            name='film_work',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='film_work', to='movies.filmwork'),
        ),
    ]