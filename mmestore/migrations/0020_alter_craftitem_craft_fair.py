# Generated by Django 3.2.7 on 2021-09-25 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("mmestore", "0019_alter_craftitem_craft_fair"),
    ]

    operations = [
        migrations.AlterField(
            model_name="craftitem",
            name="craft_fair",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="mmestore.craftfair",
            ),
        ),
    ]
