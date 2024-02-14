# Generated by Django 5.0.1 on 2024-02-01 09:40

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("clothes", "0007_delete_item"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Outer",
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
                ("outer", models.FileField(default="", upload_to="picture/")),
                ("create_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("update_at", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "coordinate",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="outers",
                        to="clothes.coordinate",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "outer",
            },
        ),
    ]