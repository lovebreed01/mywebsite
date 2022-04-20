# Generated by Django 4.0.2 on 2022-03-24 07:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment_children'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='children',
        ),
        migrations.AddField(
            model_name='comment',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.comment'),
        ),
    ]