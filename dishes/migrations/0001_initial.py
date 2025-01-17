# Generated by Django 5.0.4 on 2024-04-22 18:52

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DishesType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Тип блюда',
                'verbose_name_plural': 'Типы блюд',
                'indexes': [models.Index(fields=['name'], name='dishes_dish_name_cebe13_idx')],
                'unique_together': {('name',)},
            },
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('number_of_servings', models.IntegerField(blank=True, null=True)),
                ('is_published', models.BooleanField()),
                ('slug', models.SlugField(max_length=255)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='published_recipes', to=settings.AUTH_USER_MODEL)),
                ('dish_type', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='dishes_of_this_type', to='dishes.dishestype')),
            ],
            options={
                'verbose_name': 'Блюдо',
                'verbose_name_plural': 'Блюда',
            },
        ),
        migrations.CreateModel(
            name='MeasureUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('short_name', models.CharField(blank=True, max_length=8, null=True)),
            ],
            options={
                'verbose_name': 'Единица измерения',
                'verbose_name_plural': 'Единицы измерения',
                'indexes': [models.Index(fields=['name'], name='dishes_meas_name_5e8546_idx')],
                'unique_together': {('name',)},
            },
        ),
        migrations.CreateModel(
            name='DishProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_quantity', models.FloatField()),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='products_in_this_dish', to='dishes.dish')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dishes_with_this_product', to='products.product')),
                ('measure_unit', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='dishes.measureunit')),
            ],
            options={
                'verbose_name': 'Продукт в блюде',
                'verbose_name_plural': 'Продукты в блюдах',
            },
        ),
        migrations.CreateModel(
            name='UserDish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_of_consumption', models.DateTimeField()),
                ('weight', models.FloatField(blank=True, null=True)),
                ('number_of_servings', models.FloatField(blank=True, null=True)),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='eaten', to='dishes.dish')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eaten_dishes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Блюдо съеденое пользователем',
                'verbose_name_plural': 'Блюда съеденые пользователями',
            },
        ),
        migrations.AddIndex(
            model_name='dish',
            index=models.Index(fields=['name'], name='dishes_dish_name_e93a9d_idx'),
        ),
        migrations.AddIndex(
            model_name='dish',
            index=models.Index(fields=['-publish'], name='dishes_dish_publish_d2ce17_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='dishproducts',
            unique_together={('dish', 'product')},
        ),
        migrations.AddIndex(
            model_name='userdish',
            index=models.Index(fields=['dish'], name='dishes_user_dish_id_3683a7_idx'),
        ),
        migrations.AddIndex(
            model_name='userdish',
            index=models.Index(fields=['user'], name='dishes_user_user_id_7a44e5_idx'),
        ),
        migrations.AddIndex(
            model_name='userdish',
            index=models.Index(fields=['time_of_consumption'], name='dishes_user_time_of_d24847_idx'),
        ),
    ]
