# Generated by Django 5.0.4 on 2024-05-14 10:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0002_remove_dish_dish_type_dishtype_dish_dish_types'),
    ]

    operations = [
        migrations.CreateModel(
            name='DishToType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='dishes.dish')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='dishes.dishestype')),
            ],
        ),
        migrations.AlterField(
            model_name='dish',
            name='dish_types',
            field=models.ManyToManyField(through='dishes.DishToType', to='dishes.dishestype'),
        ),
        migrations.DeleteModel(
            name='DishType',
        ),
    ]
