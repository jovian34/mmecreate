# Generated by Django 3.2.4 on 2021-06-27 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mmestore", "0009_craftitem_pay_code"),
    ]

    operations = [
        migrations.AddField(
            model_name="craftitem",
            name="shipping",
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name="craftitem",
            name="pay_code",
            field=models.CharField(
                blank=True, default=None, max_length=10000, null=True
            ),
        ),
    ]
