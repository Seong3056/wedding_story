# Generated by Django 5.0.1 on 2024-02-14 02:55

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                (
                    "user_id",
                    models.CharField(
                        max_length=16, unique=True, verbose_name="사용자 아이디"
                    ),
                ),
            ],
        ),
    ]