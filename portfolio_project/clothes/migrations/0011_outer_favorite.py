# Generated by Django 5.0.1 on 2024-02-06 07:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("clothes", "0010_alter_coordinate_id_alter_coordinate_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="outer",
            name="favorite",
            field=models.FileField(default="", upload_to="picture/"),
        ),
    ]
