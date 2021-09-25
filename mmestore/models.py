from django.db import models
from datetime import datetime


class Category(models.Model):
    cat_name = models.CharField(max_length=200)

    def __str__(self):
        return self.cat_name


class CraftFair(models.Model):
    fair_name = models.CharField(max_length=200)
    fair_url = models.URLField(default=None, blank=True, null=True, max_length=200)
    address = models.CharField(default=None, blank=True, null=True, max_length=200)
    city = models.CharField(default=None, blank=True, null=True, max_length=200)
    state = models.CharField(default='IN', blank=True, null=True, max_length=200)
    zip = models.CharField(default=None, blank=True, null=True, max_length=20)
    first_start_time = models.DateTimeField(default=datetime.now)
    first_end_time = models.DateTimeField(default=datetime.now)
    second_start_time = models.DateTimeField(default=None, blank=True, null=True)
    second_end_time = models.DateTimeField(default=None, blank=True, null=True)
    third_start_time = models.DateTimeField(default=None, blank=True, null=True)
    third_end_time = models.DateTimeField(default=None, blank=True, null=True)
    photo_fair = models.URLField(
        default="https://live.staticflickr.com/7893/31652682857_186874f73f_w.jpg",
        blank=True,
        null=True,
        max_length=200
    )
    photo_fair_width = models.IntegerField(default=400, blank=True, null=True)
    photo_fair_height = models.IntegerField(default=300, blank=True, null=True)

    def __str__(self):
        return self.fair_name


class CraftItem(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    item_number = models.CharField(unique=True, max_length=16)
    description = models.CharField(default=None, blank=True, null=True, max_length=200)
    photo_front = models.URLField(default=None, blank=True, null=True, max_length=200)
    photo_front_width = models.IntegerField(default=None, blank=True, null=True)
    photo_front_height = models.IntegerField(default=None, blank=True, null=True)
    photo_back = models.URLField(default=None, blank=True, null=True, max_length=200)
    photo_back_width = models.IntegerField(default=None, blank=True, null=True)
    photo_back_height = models.IntegerField(default=None, blank=True, null=True)
    price = models.FloatField(default=None, blank=True, null=True)
    shipping = models.FloatField(default=None, blank=True, null=True)
    has_it_been_sold = models.BooleanField(default=False)
    width = models.FloatField(default=None, blank=True, null=True)
    height = models.FloatField(default=None, blank=True, null=True)
    depth = models.FloatField(default=None, blank=True, null=True)
    dress_size = models.FloatField(default=None, blank=True, null=True)
    pay_code = models.CharField(default=None, blank=True, null=True,  max_length=10000)
    craft_fair = models.ForeignKey(CraftFair, default=None, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.description

