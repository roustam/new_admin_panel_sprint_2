# Generated by Django 3.2 on 2023-03-02 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0008_alter_genrefilmwork_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personfilmwork',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fw_person', to='movies.person'),
        ),
        migrations.AddIndex(
            model_name='personfilmwork',
            index=models.Index(fields=['film_work', 'person'], name='film_work_person_idx'),
        ),
    ]
