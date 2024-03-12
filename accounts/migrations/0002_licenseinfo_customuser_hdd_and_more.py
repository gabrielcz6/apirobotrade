# Generated by Django 5.0.3 on 2024-03-11 13:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="LicenseInfo",
            fields=[
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("password", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "license_key",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("license_expiry_date", models.DateField(blank=True, null=True)),
                ("hdd", models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.AddField(
            model_name="customuser",
            name="hdd",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="customuser",
            name="license_expiry_date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="customuser",
            name="license_key",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
