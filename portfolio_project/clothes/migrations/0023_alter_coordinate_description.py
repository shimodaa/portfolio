# Generated by Django 5.0.2 on 2024-02-19 09:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("clothes", "0022_rename_outer_image_favorite_outer"),
    ]

    operations = [
        migrations.AlterField(
            model_name="coordinate",
            name="description",
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
