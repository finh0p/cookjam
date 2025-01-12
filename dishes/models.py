from django.db import models
from products.models import Product
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.


class DishesType(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        unique_together =(('name',),)
        indexes = [models.Index(fields=['name',]),]

        verbose_name = 'Тип блюда'
        verbose_name_plural = 'Типы блюд'

    def __str__(self):
        return self.name


class Dish(models.Model):
    
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Черновик'
        PUBLISHED = 'PB', 'Опубликовано'

    name = models.CharField(max_length=255)
    author = models.ForeignKey(User,
                               models.RESTRICT,
                               related_name='published_recipes')
    dish_types = models.ManyToManyField(DishesType, through='DishToType')
    number_of_servings = models.IntegerField(blank=True, null=True)
    is_published =  models.CharField(max_length=2,
                                     choices=Status.choices,
                                     default=Status.DRAFT)
    slug = models.SlugField(max_length=255)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [models.Index(fields=['name',]),
                   models.Index(fields=['-publish']),]

        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'

    def __str__(self):
        return f"{self.id} {self.name}"


class DishToType(models.Model):
    dish = models.ForeignKey(Dish,
                             models.RESTRICT)
    type = models.ForeignKey(DishesType,
                             models.RESTRICT)
    
    class Meta:
        unique_together = (('dish', 'type'), )


class MeasureUnit(models.Model):
    name = models.CharField(max_length=64)
    short_name = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        unique_together =(('name',), ('short_name',), )
        indexes = [models.Index(fields=['name',]),]

        verbose_name = 'Единица измерения'
        verbose_name_plural = 'Единицы измерения'

    def __str__(self):
        s = ''
        if self.short_name:
            s = self.short_name
        else:
            s = self.name
        return s


class DishProducts(models.Model):
    dish = models.ForeignKey(Dish,
                             models.RESTRICT,
                             related_name='products_in_this_dish')
    product = models.ForeignKey(Product,
                                models.CASCADE,
                                related_name='dishes_with_this_product')
    product_quantity = models.FloatField()
    measure_unit = models.ForeignKey(MeasureUnit,
                                     models.RESTRICT)

    class Meta:
        unique_together = (('dish', 'product'),)

        verbose_name = 'Продукт в блюде'
        verbose_name_plural = 'Продукты в блюдах'


class UserDish(models.Model):
    dish = models.ForeignKey(Dish,
                             models.RESTRICT,
                             related_name='eaten')
    user = models.ForeignKey(User,
                             models.CASCADE,
                             related_name='eaten_dishes')
    time_of_consumption = models.DateTimeField()
    weight = models.FloatField(blank=True, null=True)
    number_of_servings = models.FloatField(blank=True, null=True)

    class Meta:
        indexes = [models.Index(fields=['dish',]),
                   models.Index(fields=['user',]),
                   models.Index(fields=['time_of_consumption',]),]
        
        verbose_name = 'Блюдо съеденое пользователем'
        verbose_name_plural = 'Блюда съеденые пользователями'