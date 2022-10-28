# Generated by Django 4.1 on 2022-10-28 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("center", "0002_category_is_active"),
    ]

    operations = [
        migrations.CreateModel(
            name="Announcement",
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
                ("title", models.CharField(max_length=100)),
                ("content", models.TextField()),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to="images/anouncements/"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="NewsFeed",
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
                ("title", models.CharField(max_length=100)),
                ("author", models.CharField(blank=True, max_length=100, null=True)),
                ("content", models.TextField()),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to="images/newsfeed/"
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
