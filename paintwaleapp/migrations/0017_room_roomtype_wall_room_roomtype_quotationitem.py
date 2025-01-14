# Generated by Django 4.2.17 on 2025-01-14 03:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("paintwaleapp", "0016_lead_city"),
    ]

    operations = [
        migrations.CreateModel(
            name="Room",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "lead",
                    models.ForeignKey(
                        db_column="lead_id",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="paintwaleapp.lead",
                    ),
                ),
            ],
            options={
                "db_table": "room",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="RoomType",
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
                    "room_type",
                    models.CharField(
                        blank=True, default=None, max_length=100, null=True
                    ),
                ),
                ("active", models.BooleanField(blank=True, default=True, null=True)),
            ],
            options={
                "db_table": "room_type",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="Wall",
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
                    "wall_type",
                    models.CharField(
                        blank=True, default=None, max_length=255, null=True
                    ),
                ),
                ("add_area", models.FloatField(blank=True, default=None, null=True)),
                ("sub_area", models.FloatField(blank=True, default=None, null=True)),
                ("total_area", models.FloatField(blank=True, default=None, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "room",
                    models.ForeignKey(
                        db_column="room_id",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="paintwaleapp.room",
                    ),
                ),
            ],
            options={
                "db_table": "wall",
                "managed": True,
            },
        ),
        migrations.AddField(
            model_name="room",
            name="roomtype",
            field=models.ForeignKey(
                db_column="roomtype_id",
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="paintwaleapp.roomtype",
            ),
        ),
        migrations.CreateModel(
            name="QuotationItem",
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
                ("total_area", models.FloatField(blank=True, default=None, null=True)),
                (
                    "wall_type",
                    models.CharField(
                        blank=True, default=None, max_length=255, null=True
                    ),
                ),
                ("price", models.FloatField(blank=True, default=None, null=True)),
                ("discount", models.FloatField(blank=True, default=None, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "created_by",
                    models.ForeignKey(
                        db_column="created_by",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="createdquotationtem",
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
                    "quotation",
                    models.ForeignKey(
                        db_column="quotation_id",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="paintwaleapp.quotation",
                    ),
                ),
                (
                    "wall",
                    models.ForeignKey(
                        db_column="wall_id",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="paintwaleapp.wall",
                    ),
                ),
            ],
            options={
                "db_table": "quotation_item",
                "managed": True,
            },
        ),
    ]
