# Generated by Django 4.0.2 on 2022-04-08 04:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_remove_comment_parent_post_updated'),
    ]

    operations = [
        migrations.RenameField(
            model_name='music',
            old_name='file',
            new_name='music_file',
        ),
    ]
