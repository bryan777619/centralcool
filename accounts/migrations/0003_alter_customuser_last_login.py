# Generated by Django 5.0.7 on 2024-10-20 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_customuser_is_admin"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="last_login",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
