# Generated by Django 4.0.2 on 2022-04-04 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_music_artist_alter_music_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='parent',
        ),
        migrations.AddField(
            model_name='post',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
