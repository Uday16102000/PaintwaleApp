# Generated by Django 4.2.17 on 2025-01-14 02:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("paintwaleapp", "0010_users"),
    ]

    operations = [
        migrations.CreateModel(
            name="City",
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
                (
                    "city_name",
                    models.CharField(
                        blank=True, default=None, max_length=100, null=True
                    ),
                ),
                (
                    "city_code",
                    models.CharField(
                        blank=True, default=None, max_length=20, null=True
                    ),
                ),
                ("active", models.BooleanField(blank=True, default=True, null=True)),
            ],
            options={
                "db_table": "city",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="PriceList",
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
                ("price", models.FloatField(blank=True, default=None, null=True)),
                (
                    "is_lumpsum_rate",
                    models.IntegerField(blank=True, default=0, null=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
                (
                    "city",
                    models.ForeignKey(
                        db_column="city_id",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="paintwaleapp.city",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        db_column="created_by",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="createdpricelist",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "process",
                    models.ForeignKey(
                        db_column="process_id",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="paintwaleapp.process",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        db_column="product_id",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="paintwaleapp.product",
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        db_column="updated_by",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="updatedpricelist",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "price_list",
                "managed": True,
            },
        ),
        migrations.AddConstraint(
            model_name="pricelist",
            constraint=models.UniqueConstraint(
                fields=("process", "product", "city"),
                name="unique_process_product_city",
            ),
        ),
    ]
