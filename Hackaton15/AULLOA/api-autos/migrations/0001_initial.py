# Generated by Django 4.2.2 on 2023-06-17 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(default='', max_length=50)),
                ('year', models.IntegerField()),
                ('modelo', models.CharField(max_length=150)),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_autos.marca')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_autos.tipo')),
            ],
        ),
    ]