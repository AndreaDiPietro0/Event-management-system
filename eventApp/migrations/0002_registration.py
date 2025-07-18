# Generated by Django 4.2.23 on 2025-07-04 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("eventApp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Registration",
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
                ("user_name", models.CharField(max_length=100)),
                ("user_email", models.EmailField(max_length=254)),
                ("user_phone", models.CharField(max_length=10)),
                ("registration_date", models.DateField(auto_now_add=True)),
                (
                    "event_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="eventApp.event"
                    ),
                ),
            ],
        ),
    ]
