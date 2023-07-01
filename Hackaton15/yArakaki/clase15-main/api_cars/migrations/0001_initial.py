# Generated by Django 4.2.2 on 2023-06-17 00:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Marca",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Tipo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Auto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("modelo", models.CharField(max_length=100)),
                ("color", models.CharField(max_length=100)),
                ("anio", models.IntegerField()),
                ("img_apth", models.CharField(default="", max_length=500, null=True)),
                (
                    "marca",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api_cars.marca"
                    ),
                ),
                (
                    "tipo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api_cars.tipo"
                    ),
                ),
            ],
        ),
    ]