# Generated by Django 5.0.2 on 2024-02-22 12:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("clothes", "0023_alter_coordinate_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="coordinate",
            name="counter",
            field=models.IntegerField(default=0),
        ),
    ]
