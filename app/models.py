from django.db import models
from django.contrib.auth.models import User


class Phones(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name='Модель')
    image = models.CharField(max_length=50, verbose_name='Изображение')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    description = models.CharField(max_length=100, verbose_name='Описание')
    slug = models.SlugField(max_length=50)


class Review(models.Model):
    name = models.TextField()
    content = models.TextField()
    product = models.ForeignKey(Phones, on_delete=models.CASCADE)


class Cart(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.ForeignKey(Phones, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=None)
