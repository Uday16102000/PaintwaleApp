# Generated by Django 4.2.17 on 2025-01-13 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("paintwaleapp", "0004_productbrand_servicetype_product_process"),
    ]

    operations = [
        migrations.AlterField(
            model_name="servicetype",
            name="service_name",
            field=models.CharField(default="", max_length=255, unique=True),
            preserve_default=False,
        ),
    ]