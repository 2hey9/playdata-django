# Generated by Django 4.2.1 on 2023-05-15 02:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pybo", "0006_auto_20200507_1449"),
    ]

    operations = [
        migrations.AddField(
            model_name="question",
            name="likes",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
