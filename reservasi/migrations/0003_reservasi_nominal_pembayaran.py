# Generated by Django 5.0.7 on 2024-12-05 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "reservasi",
            "0002_acproblem_carbrand_cartype_alter_reservasi_options_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="reservasi",
            name="nominal_pembayaran",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True
            ),
        ),
    ]
