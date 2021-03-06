# Generated by Django 4.0.2 on 2022-03-27 04:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_musiccategory_music_image_alter_music_artist_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.artist'),
        ),
        migrations.AlterField(
            model_name='music',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.musiccategory'),
            preserve_default=False,
        ),
    ]
