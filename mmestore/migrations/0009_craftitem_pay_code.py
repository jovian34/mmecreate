# Generated by Django 3.1.2 on 2020-11-11 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mmestore", "0008_auto_20201107_1845"),
    ]

    operations = [
        migrations.AddField(
            model_name="craftitem",
            name="pay_code",
            field=models.CharField(
                blank=True, default=None, max_length=1000, null=True
            ),
        ),
    ]
