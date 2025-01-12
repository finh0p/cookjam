from django.db import models

# Create your models here.


# Модели для приложения products
class AcidCompositionInformations(models.Model):
    tryptophan = models.FloatField(null=True, blank=True)
    threonine = models.FloatField(null=True, blank=True)
    isoleucine = models.FloatField(null=True, blank=True)
    leucine = models.FloatField(null=True, blank=True)
    lysine = models.FloatField(null=True, blank=True)
    methionine = models.FloatField(null=True, blank=True)
    cysteine = models.FloatField(null=True, blank=True)
    phenylalanine = models.FloatField(null=True, blank=True)
    tyrosine = models.FloatField(null=True, blank=True)
    valin = models.FloatField(null=True, blank=True)
    arginine = models.FloatField(null=True, blank=True)
    histidine = models.FloatField(null=True, blank=True)
    alanin = models.FloatField(null=True, blank=True)
    aspartic_acid = models.FloatField(null=True, blank=True)
    glutamic_acid = models.FloatField(null=True, blank=True)
    glycine = models.FloatField(null=True, blank=True)
    proline = models.FloatField(null=True, blank=True)
    serin = models.FloatField(null=True, blank=True)
    omega3 = models.FloatField(null=True, blank=True)

    class Meta:
        verbose_name = 'Информация о содержании аминокислот в продукте'
        verbose_name_plural = 'Информация о содержании аминокислот в продуктах'


class VitaminsInformations(models.Model):
    vitamin_a = models.FloatField(null=True, blank=True)
    alpha_carotene = models.FloatField(null=True, blank=True)
    beta_carotene = models.FloatField(null=True, blank=True)
    vitamin_d = models.FloatField(null=True, blank=True)
    vitamin_e = models.FloatField(null=True, blank=True)
    vitamin_k = models.FloatField(null=True, blank=True)
    vitamin_c = models.FloatField(null=True, blank=True)
    vitamin_b1 = models.FloatField(null=True, blank=True)
    vitamin_b2 = models.FloatField(null=True, blank=True)
    vitamin_b3 = models.FloatField(null=True, blank=True)
    vitamin_b4 = models.FloatField(null=True, blank=True)
    vitamin_b5 = models.FloatField(null=True, blank=True)
    vitamin_b6 = models.FloatField(null=True, blank=True)
    vitamin_b7 = models.FloatField(null=True, blank=True)
    vitamin_b8 = models.FloatField(null=True, blank=True)
    vitamin_b9 = models.FloatField(null=True, blank=True)
    vitamin_b11 = models.FloatField(null=True, blank=True)
    vitamin_b12 = models.FloatField(null=True, blank=True)
    vitamin_b13 = models.FloatField(null=True, blank=True)
    coenzyme_q10 = models.FloatField(null=True, blank=True)
    vitamin_n = models.FloatField(null=True, blank=True)
    vitamin_u = models.FloatField(null=True, blank=True)

    class Meta:
        verbose_name = 'Информация о содержании витаминов в продукте'
        verbose_name_plural = 'Информация о содержании витаминов в продуктах'


class MicroelementsInformations(models.Model):
    ca = models.FloatField(null=True, blank=True)
    fe = models.FloatField(null=True, blank=True)
    i = models.FloatField(null=True, blank=True)
    mg = models.FloatField(null=True, blank=True)
    p = models.FloatField(null=True, blank=True)
    k = models.FloatField(null=True, blank=True)
    na = models.FloatField(null=True, blank=True)
    zn = models.FloatField(null=True, blank=True)
    cu = models.FloatField(null=True, blank=True)
    mn = models.FloatField(null=True, blank=True)
    se = models.FloatField(null=True, blank=True)
    f = models.FloatField(null=True, blank=True)
    cr = models.FloatField(null=True, blank=True)
    si = models.FloatField(null=True, blank=True)
    cl = models.FloatField(null=True, blank=True)
    mo = models.FloatField(null=True, blank=True)
    s = models.FloatField(null=True, blank=True)

    class Meta:
        verbose_name = 'Информация о содержании микроэлементов в продукте'
        verbose_name_plural = 'Информация о содержании микроэлементов в продуктах'


class ProductsMainInformation(models.Model):
    proteins = models.FloatField(null=True, blank=True)
    fats = models.FloatField(null=True, blank=True)
    carbohydrates = models.FloatField(null=True, blank=True)
    kcal = models.FloatField(null=True, blank=True)
    water = models.FloatField(null=True, blank=True)
    fiber = models.FloatField(null=True, blank=True)
    starch = models.FloatField(null=True, blank=True)
    cholesterol = models.FloatField(null=True, blank=True)
    trans_fats = models.FloatField(null=True, blank=True)

    class Meta:
        verbose_name = 'Основная информация о продукте'
        verbose_name_plural = 'Основная информация о продуктах'


class DiabetesInformations(models.Model):
    glycemic_index = models.IntegerField(null=True, blank=True)
    insulin_index = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = 'Информация для диабетиков о продукте'
        verbose_name_plural = 'Информация для диабетиков о продуктах'


class ProductsCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = (('name',),)
        indexes = [models.Index(fields=['name',]),]
        
        verbose_name = 'Категория продуктов'
        verbose_name_plural = 'Категории продуктов'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    categories = models.ManyToManyField(ProductsCategory,
                                        through="ProductToCategory",
                                        blank=True,
                                        null=True)
    slug = models.SlugField(max_length=255)
    main_information = models.ForeignKey(ProductsMainInformation, models.RESTRICT)
    diabetes_information = models.ForeignKey(DiabetesInformations, models.RESTRICT)
    vitamins_information = models.ForeignKey(VitaminsInformations, models.RESTRICT)
    microelements_information = models.ForeignKey(MicroelementsInformations, models.RESTRICT)
    acid_composition = models.ForeignKey(AcidCompositionInformations, models.RESTRICT)

    class Meta:
        unique_together =(('name',),)
        indexes = [models.Index(fields=['name',]),]

        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f"{self.name}"
    

class ProductToCategory(models.Model):
    product = models.ForeignKey(Product,
                                models.RESTRICT)
    category = models.ForeignKey(ProductsCategory,
                                 models.RESTRICT)
    
    class Meta:
        unique_together = (('product','category'),)

