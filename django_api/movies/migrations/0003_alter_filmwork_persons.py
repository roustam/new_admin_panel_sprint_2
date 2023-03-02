# Generated by Django 3.2 on 2023-03-01 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20230301_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filmwork',
            name='persons',
            field=models.ManyToManyField(related_name='filmworks', through='movies.PersonFilmwork', to='movies.Person'),
        ),
    ]
