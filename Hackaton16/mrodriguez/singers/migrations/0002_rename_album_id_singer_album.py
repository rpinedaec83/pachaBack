# Generated by Django 4.2.2 on 2023-06-27 06:30

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("singers", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="singer",
            old_name="album_id",
            new_name="album",
        ),
    ]
