# Generated by Django 5.0.1 on 2024-02-07 08:00

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("clothes", "0017_remove_outer_favorite_favorite"),
    ]

    operations = [
        migrations.RenameField(
            model_name="favorite",
            old_name="outer",
            new_name="outer1",
        ),
    ]
