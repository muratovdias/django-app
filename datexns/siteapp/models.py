from django.db import models
# from django.contrib.auth import get_user_model
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя категории')
    slug = models.SlugField(unique=True)
    image = models.ImageField(max_length=50, blank=True, verbose_name='Изображение')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']


class Product(models.Model):

    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Наименование')
    slug = models.SlugField(unique=True)
    image = models.ImageField(verbose_name='Изображение')
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    description2 = models.TextField(verbose_name='Характеристики', null=True, blank=True)
    price = models.DecimalField(max_digits=9, decimal_places=0, verbose_name='Цена')
    is_published = models.BooleanField(default=True, verbose_name='В наличии')

    def __str__(self):
        return self.title

    # def get_model_name(self):
    #     return self.__class__.__name__.lower()

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'prod_slug': self.slug})

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['id']


