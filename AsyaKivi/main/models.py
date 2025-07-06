from django.db import models

class Session(models.Model):
    """
     Session - данные о сессии, которые создаются django. В данном примере выступает в роли корзины.
     Для избежания коллизии нужно чистить раз в неделю-месяц
    """

    session_key = models.CharField(max_length=32, primary_key=True, verbose_name="Session Id")
    user_agent = models.CharField(max_length=255, null=True, blank=True, verbose_name="User-Agent")
    ip = models.CharField(max_length=255, null=True, blank=True, verbose_name="Ip")

    last_visit = models.DateTimeField(auto_now=True, verbose_name='Дата последнего посещения')

class Category(models.Model):
    id = models.AutoField(verbose_name='Идентификатор', primary_key=True)
    title = models.CharField(verbose_name='Категория', max_length=255)


class Collection(models.Model):
    id = models.AutoField(verbose_name='Идентификатор', primary_key=True)

    title = models.CharField(verbose_name='Коллекция', max_length=255)
    items = models.ManyToManyField('Item', verbose_name='Товары', through='ItemCollection')


class Item(models.Model):
    id = models.AutoField(verbose_name='Идентификатор', primary_key=True)
    name = models.CharField(verbose_name='Название', max_length=255)
    code = models.CharField(verbose_name='Код', max_length=30, null=False, blank=False, unique=True) # состоит из страницы и номера на странице

    description = models.TextField(verbose_name='Описание')

    amount = models.IntegerField(verbose_name='Колличество', default=0)
    price = models.FloatField(verbose_name='Цена', default=0)

    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        indexes = [
            models.Index(fields=['code']),
            models.Index(fields=['category'])
        ]


class ItemCollection(models.Model):
    item = models.ForeignKey(Item, verbose_name='Товар', on_delete=models.CASCADE)
    collection = models.ForeignKey(Collection, verbose_name='Коллекция', on_delete=models.CASCADE)


class ItemImage(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name='Товар')

    image = models.ImageField(
        upload_to='images/items',
        verbose_name='Картинка'
    )

class CollectionImage(models.Model):
    collection = models.ForeignKey(Collection, verbose_name='Коллекция', on_delete=models.CASCADE)

    image = models.ImageField(
        upload_to='images/collections',
        verbose_name='Картинка'
    )

class CartItem(models.Model):
    session = models.ForeignKey(Session, verbose_name='Пользователь(сессия)', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, verbose_name='Товар', on_delete=models.CASCADE)
    amount = models.IntegerField(verbose_name='Колличество', default=1)
