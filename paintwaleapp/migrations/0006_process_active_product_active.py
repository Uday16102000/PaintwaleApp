# Generated by Django 4.2.17 on 2025-01-13 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("paintwaleapp", "0005_alter_servicetype_service_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="process",
            name="active",
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name="product",
            name="active",
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]