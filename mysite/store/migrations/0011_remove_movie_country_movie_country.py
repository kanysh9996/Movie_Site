# Generated by Django 5.1.5 on 2025-01-24 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_rename_movie_favoritemovie_movie_favorite_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='country',
        ),
        migrations.AddField(
            model_name='movie',
            name='country',
            field=models.ManyToManyField(related_name='country', to='store.country'),
        ),
    ]
