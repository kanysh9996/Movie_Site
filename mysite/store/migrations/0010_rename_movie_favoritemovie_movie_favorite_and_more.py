# Generated by Django 5.1.5 on 2025-01-23 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_alter_favorite_user_alter_favoritemovie_cart_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='favoritemovie',
            old_name='movie',
            new_name='movie_favorite',
        ),
        migrations.RenameField(
            model_name='history',
            old_name='movie',
            new_name='movie_history',
        ),
        migrations.RenameField(
            model_name='movielanguages',
            old_name='movie',
            new_name='movie_language',
        ),
        migrations.RenameField(
            model_name='rating',
            old_name='movie',
            new_name='movie_rating',
        ),
    ]
