# Generated by Django 4.2.16 on 2024-11-26 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='social_links',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='video_links',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='web_links',
            field=models.URLField(blank=True),
        ),
    ]
