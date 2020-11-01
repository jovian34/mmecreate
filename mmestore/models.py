from django.db import models


class Category(models.Model):
    cat_name = models.CharField(max_length=200)
    item_range_min = models.IntegerField()
    item_range_max = models.IntegerField()

    def __str__(self):
        return self.cat_name


class CraftItem(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    photo_front = models.URLField(max_length=200)
    photo_back = models.URLField(max_length=200)
    price = models.FloatField()
    has_it_been_sold = models.BooleanField()
    item_number = models.IntegerField(unique=True)
    width = models.FloatField()
    height = models.FloatField()
    depth = models.FloatField()

    def __str__(self):
        return self.description

