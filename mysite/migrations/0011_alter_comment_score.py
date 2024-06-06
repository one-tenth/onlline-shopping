# Generated by Django 4.2.5 on 2024-06-06 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0010_alter_comment_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='score',
            field=models.IntegerField(choices=[('onestar', '★'), ('twostar', '★★'), ('threestar', '★★★'), ('fourstar', '★★★★'), ('fivestar', '★★★★★')]),
        ),
    ]
