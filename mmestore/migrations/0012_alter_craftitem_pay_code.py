# Generated by Django 3.2.4 on 2021-08-06 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mmestore", "0011_craftfair"),
    ]

    operations = [
        migrations.AlterField(
            model_name="craftitem",
            name="pay_code",
            field=models.CharField(
                blank=True, default=None, max_length=10001, null=True
            ),
        ),
    ]
