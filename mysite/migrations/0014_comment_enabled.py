# Generated by Django 4.2.5 on 2024-06-07 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0013_remove_comment_order_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='enabled',
            field=models.BooleanField(default=True),
        ),
    ]
