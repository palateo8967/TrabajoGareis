# Generated by Django 5.2 on 2025-04-04 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0002_alter_productos_codigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='Codigo',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
