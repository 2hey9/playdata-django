# Generated by Django 4.2.1 on 2023-05-15 06:01

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("pybo", "0007_question_likes"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="question",
            name="likes",
        ),
    ]
