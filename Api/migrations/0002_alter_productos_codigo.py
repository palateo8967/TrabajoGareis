# Generated by Django 5.2 on 2025-04-04 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='Codigo',
            field=models.IntegerField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
