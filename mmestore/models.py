from django.db import models


class Category(models.Model):
    cat_name = models.CharField(max_length=200)

    def __str__(self):
        return self.cat_name


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
    has_it_been_sold = models.BooleanField(default=False)
    width = models.FloatField(default=None, blank=True, null=True)
    height = models.FloatField(default=None, blank=True, null=True)
    depth = models.FloatField(default=None, blank=True, null=True)
    dress_size = models.FloatField(default=None, blank=True, null=True)

    def __str__(self):
        return self.description

