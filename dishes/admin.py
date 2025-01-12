from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.DishesType)
class DishesTypeAdmin(admin.ModelAdmin):
    list_display = ['name',]
    list_filter = ['name',]


@admin.register(models.Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'is_published',]
    list_display_links = ['name','author',]
    list_filter = ['name', 'author', 'is_published',]
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['name',]
    raw_id_fields = ['author',]


@admin.register(models.MeasureUnit)
class MeasureUnit(admin.ModelAdmin):
    list_display = ['name', 'short_name',]
    list_filter = ['name',]
    ordering = ['name',]


@admin.register(models.DishProducts)
class DishProductsAdmin(admin.ModelAdmin):
    list_display = ['dish', 'product', 'product_quantity', 'measure_unit',]
    list_display_link = ['dish', 'product',]
    list_filter = ['dish', 'product',]
    raw_id_fields = ['dish', 'product', 'measure_unit',]


@admin.register(models.UserDish)
class UserDishAdmin(admin.ModelAdmin):
    list_display = ['dish',
                    'user',
                    'time_of_consumption',
                    'weight',
                    'number_of_servings',]
    list_display_links = ['dish', 'user',]
    list_filter = ['dish', 'user',]
    raw_id_fields = ['dish', 'user',]
    ordering = ['-time_of_consumption',]


@admin.register(models.DishToType)
class DishToTypeAdmin(admin.ModelAdmin):
    list_display = ['dish', 'type',]
    list_filter = ['dish', 'type',]
    raw_id_fields = ['dish', 'type',]
