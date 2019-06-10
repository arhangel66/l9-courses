# Generated by Django 2.2.2 on 2019-06-06 03:35

from django.conf import settings
from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]

    operations = [
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    django_extensions.db.fields.CreationDateTimeField(
                        auto_now_add=True, verbose_name="created"
                    ),
                ),
                (
                    "modified",
                    django_extensions.db.fields.ModificationDateTimeField(
                        auto_now=True, verbose_name="modified"
                    ),
                ),
                ("title", models.CharField(max_length=255, verbose_name="title")),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="description"),
                ),
                (
                    "students",
                    models.ManyToManyField(
                        blank=True,
                        related_name="student_courses",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="students",
                    ),
                ),
                (
                    "teachers",
                    models.ManyToManyField(
                        blank=True,
                        related_name="teacher_courses",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="teachers",
                    ),
                ),
            ],
            options={"verbose_name_plural": "courses"},
        )
    ]