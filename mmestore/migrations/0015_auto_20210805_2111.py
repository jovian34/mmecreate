# Generated by Django 3.2.4 on 2021-08-06 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mmestore", "0014_auto_20210805_2038"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="craftfair",
            name="second_date",
        ),
        migrations.RemoveField(
            model_name="craftfair",
            name="start_date",
        ),
        migrations.RemoveField(
            model_name="craftfair",
            name="third_date",
        ),
        migrations.AddField(
            model_name="craftfair",
            name="fair_url",
            field=models.URLField(blank=True, default=None, null=True),
        ),
    ]
