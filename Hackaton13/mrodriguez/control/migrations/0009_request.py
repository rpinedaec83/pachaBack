# Generated by Django 4.2.1 on 2023-06-02 22:26

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("control", "0008_alter_attendancerecord_student"),
    ]

    operations = [
        migrations.CreateModel(
            name="Request",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("fullname", models.CharField(default="", max_length=200)),
                ("id_card_number", models.CharField(max_length=20)),
                ("email", models.CharField(max_length=100)),
                ("phone", models.BigIntegerField(blank=True, null=True)),
                ("description", models.CharField(max_length=200, null=True)),
                ("creation_date", models.DateField(default=django.utils.timezone.now)),
                (
                    "id_card_type",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="control.idcardtype",
                    ),
                ),
            ],
        ),
    ]