# Generated by Django 4.2.6 on 2023-10-14 10:11

import blogpost.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blogpost", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="image_url",
            field=models.ImageField(
                blank=True, null=True, upload_to=blogpost.models.upload_to
            ),
        ),
    ]
