# Generated by Django 4.2.5 on 2024-06-07 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0011_alter_comment_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='score',
            field=models.CharField(choices=[('onestar', '★'), ('twostar', '★★'), ('threestar', '★★★'), ('fourstar', '★★★★'), ('fivestar', '★★★★★')], max_length=10),
        ),
    ]