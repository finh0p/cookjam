from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.AcidCompositionInformations)
class AcidCompositionInformationAdmmin(admin.ModelAdmin):
    list_display = ['tryptophan', 'threonine', 'omega3',]


@admin.register(models.DiabetesInformations)
class DiabetesInformationsAdmin(admin.ModelAdmin):
    list_display = ['glycemic_index', 'insulin_index',]
    list_filter = ['glycemic_index', 'insulin_index',]


@admin.register(models.MicroelementsInformations)
class MicroelementsInformationsAdmin(admin.ModelAdmin):
    list_display = ['ca', 'fe', 'i', 'mg', 'mn', 'f',]


@admin.register(models.VitaminsInformations)
class VitaminsInformationsAdmin(admin.ModelAdmin):
    list_display = ['vitamin_a',
                    'vitamin_c',
                    'vitamin_d',
                    'alpha_carotene',
                    'beta_carotene',]
    

@admin.register(models.ProductsMainInformation)
class ProductsMainInformation(admin.ModelAdmin):
    list_display = ['proteins', 'fats', 'carbohydrates', 'kcal',]


@admin.register(models.ProductsCategory)
class ProductsCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description',]
    list_filter = ['name',]
    search_fields = ['name',]


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name',]
    list_display_link = ['name',]
    list_filter = ['name',]
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name',]
    ordering = ['name',]
    raw_id_fields = ['main_information',
                     'diabetes_information',
                     'vitamins_information',
                     'microelements_information',
                     'acid_composition',]
    

@admin.register(models.ProductToCategory)
class ProductToCategoryAdmin(admin.ModelAdmin):
    list_display = ['product', 'category']
    list_filter = ['product', 'category']
    row_id_fields = ['product', 'category']
