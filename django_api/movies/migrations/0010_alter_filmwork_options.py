# Generated by Django 3.2 on 2023-03-02 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0009_auto_20230302_1222'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='filmwork',
            options={'ordering': ['title'], 'verbose_name': 'Кинопроизведение', 'verbose_name_plural': 'Кинопроизведения'},
        ),
    ]
