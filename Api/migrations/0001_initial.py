# Generated by Django 5.1.7 on 2025-04-04 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('Codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('Nombre', models.TextField(max_length=20)),
                ('Precio', models.FloatField(max_length=10)),
                ('Marca', models.TextField(max_length=20)),
                ('Descripcion', models.TextField(max_length=100)),
            ],
        ),
    ]
