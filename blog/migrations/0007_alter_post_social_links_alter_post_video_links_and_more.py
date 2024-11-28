# Generated by Django 4.2.16 on 2024-11-28 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_comment_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='social_links',
            field=models.URLField(blank=True, default='https://example.com'),
        ),
        migrations.AlterField(
            model_name='post',
            name='video_links',
            field=models.URLField(blank=True, default='https://example.com'),
        ),
        migrations.AlterField(
            model_name='post',
            name='web_links',
            field=models.URLField(blank=True, default='https://example.com'),
        ),
    ]