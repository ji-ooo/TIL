# Generated by Django 4.2.11 on 2024-04-21 05:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_alter_movie_like_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='movie_save',
            new_name='movie',
        ),
    ]
