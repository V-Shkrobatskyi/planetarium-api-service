# Generated by Django 5.0.6 on 2024-06-21 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("planetarium", "0002_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="astronomyshow",
            old_name="show_theme",
            new_name="show_themes",
        ),
    ]
