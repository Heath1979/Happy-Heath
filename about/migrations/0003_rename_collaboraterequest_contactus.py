# Generated by Django 4.2.16 on 2024-12-11 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_collaboraterequest'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CollaborateRequest',
            new_name='ContactUs',
        ),
    ]