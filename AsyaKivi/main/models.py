from PIL.ImageEnhance import Color
from django.db import models

# Create your models here.
class Item(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()

    amount = models.IntegerField()

    colors = models.ManyToManyField('Color', through='ColorRequirement')


class ItemImage(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    image = models.ImageField(
        upload_to='images/items',
        verbose_name='картинка'
    )


class ColorRequirement(models.Model):
    colors = models.ForeignKey('Color', on_delete=models.CASCADE)
    items = models.ForeignKey(Item, on_delete=models.CASCADE)

    amount = models.IntegerField()


class Color(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    amount = models.IntegerField()