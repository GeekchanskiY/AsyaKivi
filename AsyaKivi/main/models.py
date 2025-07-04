from django.db import models


class Category(models.Model):
    id = models.AutoField(verbose_name='Идентификатор', primary_key=True)
    title = models.CharField(verbose_name='Категория', max_length=255)


class Collection(models.Model):
    id = models.AutoField(verbose_name='Идентификатор', primary_key=True)

    title = models.CharField(verbose_name='Коллекция', max_length=255)
    items = models.ManyToManyField('Item', verbose_name='Коллекции вышивашек', through='ItemCollection')


class Item(models.Model):
    id = models.AutoField(verbose_name='Идентификатор', primary_key=True)
    name = models.CharField(verbose_name='Название', max_length=255)
    description = models.TextField(verbose_name='Описание')

    amount = models.IntegerField(verbose_name='Колличество', default=0)
    price = models.FloatField(verbose_name='Цена', default=0)

    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE, blank=True, null=True)


class ItemCollection(models.Model):
    item = models.ForeignKey(Item, verbose_name='Вышивашка', on_delete=models.CASCADE)
    collection = models.ForeignKey(Collection, verbose_name='Коллекция', on_delete=models.CASCADE)


class ItemImage(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    image = models.ImageField(
        upload_to='images/items',
        verbose_name='картинка'
    )