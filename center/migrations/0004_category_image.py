# Generated by Django 4.1 on 2022-10-28 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("center", "0003_announcement_newsfeed"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="images/categories/"
            ),
        ),
    ]