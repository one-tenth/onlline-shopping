# Generated by Django 4.1 on 2024-05-05 13:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mysite", "0002_rename_membernum_member_memberid"),
    ]

    operations = [
        migrations.CreateModel(
            name="Book",
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
                ("title", models.CharField(max_length=100)),
                ("author", models.CharField(max_length=50)),
                ("published_date", models.DateField()),
            ],
        ),
    ]
