# Generated by Django 4.2.17 on 2024-12-10 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("reservasi", "0006_alter_recommendation_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="recommendation",
            options={
                "verbose_name": "Rekomendasi",
                "verbose_name_plural": "Rekomendasi",
            },
        ),
    ]