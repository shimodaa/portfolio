# Generated by Django 4.1 on 2024-01-19 16:08

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Coordinate",
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
                ("create_at", models.DateTimeField()),
                ("update_at", models.DateTimeField()),
                ("name", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=100)),
                ("outer", models.FileField(upload_to="picture/")),
            ],
            options={
                "db_table": "coordinate",
            },
        ),
        migrations.CreateModel(
            name="Item",
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
                ("create_at", models.DateTimeField()),
                ("update_at", models.DateTimeField()),
                ("outer", models.FileField(upload_to="picture/")),
            ],
            options={
                "db_table": "item",
            },
        ),
    ]
