# Generated by Django 3.1.2 on 2020-11-07 23:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mmestore', '0007_craftitem_dress_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='item_range_max',
        ),
        migrations.RemoveField(
            model_name='category',
            name='item_range_min',
        ),
    ]