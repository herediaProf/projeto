# Generated by Django 5.1.4 on 2024-12-26 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Person",
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
                ("first_name", models.CharField(max_length=30)),
                ("last_name", models.CharField(max_length=30)),
                ("age", models.IntegerField()),
                ("salary", models.DecimalField(decimal_places=2, max_digits=5)),
                ("bio", models.TextField()),
            ],
        ),
    ]
