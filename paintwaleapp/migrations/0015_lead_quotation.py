# Generated by Django 4.2.17 on 2025-01-14 03:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("paintwaleapp", "0014_users_is_staff_users_is_superuser"),
    ]

    operations = [
        migrations.CreateModel(
            name="Lead",
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
                    "name",
                    models.CharField(
                        blank=True, default=None, max_length=255, null=True
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        blank=True, default=None, max_length=20, null=True
                    ),
                ),
                (
                    "alternate_phone",
                    models.CharField(
                        blank=True, default=None, max_length=20, null=True
                    ),
                ),
                (
                    "email",
                    models.CharField(
                        blank=True, default=None, max_length=50, null=True
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Pending", "Pending"),
                            ("Measurement Done", "Measurement Done"),
                            ("Quotation sent", "Quotation sent"),
                            ("Re-Schedule", "Re-Schedule"),
                            ("Rejected", "Rejected"),
                            ("Call Back Requested", "Call Back Requested"),
                            ("Accepted", "Accepted"),
                        ],
                        default=None,
                        max_length=50,
                        null=True,
                    ),
                ),
                (
                    "landmark",
                    models.CharField(
                        blank=True, default=None, max_length=255, null=True
                    ),
                ),
                (
                    "visit_date_time",
                    models.DateTimeField(blank=True, default=None, null=True),
                ),
                (
                    "re_schedule_time",
                    models.DateTimeField(blank=True, default=None, null=True),
                ),
                (
                    "channel",
                    models.CharField(
                        blank=True, default=None, max_length=255, null=True
                    ),
                ),
                (
                    "channel_reference",
                    models.CharField(
                        blank=True, default=None, max_length=255, null=True
                    ),
                ),
                (
                    "project_type",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Interior Painting", "Interior Painting"),
                            ("Exterior Painting", "Exterior Painting"),
                            ("Waterproofing", "Waterproofing"),
                            ("OTHER", "OTHER"),
                        ],
                        default=None,
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "house_type",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("1 BHK", "1 BHK"),
                            ("2 BHK", "2 BHK"),
                            ("3 BHK", "3 BHK"),
                            ("Row House", "Row House"),
                            ("Independent Villa", "Independent Villa"),
                        ],
                        default=None,
                        max_length=255,
                        null=True,
                    ),
                ),
                ("address", models.TextField(blank=True, default=None, null=True)),
                ("remarks", models.TextField(blank=True, default=None, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
                (
                    "updated_by",
                    models.ForeignKey(
                        db_column="updated_by",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="updatedlead",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "lead",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="Quotation",
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
                    "quotation_value",
                    models.FloatField(blank=True, default=None, null=True),
                ),
                ("discount", models.FloatField(blank=True, default=None, null=True)),
                ("status", models.BooleanField(blank=True, default=None, null=True)),
                (
                    "accepted_at",
                    models.DateTimeField(blank=True, default=None, null=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
                (
                    "brand",
                    models.ForeignKey(
                        blank=True,
                        db_column="brand_id",
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="paintwaleapp.productbrand",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        db_column="created_by",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="createdquotation",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "lead",
                    models.ForeignKey(
                        db_column="lead_id",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="paintwaleapp.lead",
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        db_column="updated_by",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="updatedquotation",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "quotation",
                "managed": True,
            },
        ),
    ]
