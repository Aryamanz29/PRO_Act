# Generated by Django 3.1.7 on 2021-05-06 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_project_add_proj_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="image",
            field=models.ImageField(default="default.png", upload_to="profile_pics"),
        ),
    ]