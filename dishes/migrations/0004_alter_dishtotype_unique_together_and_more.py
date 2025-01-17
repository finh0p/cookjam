# Generated by Django 5.0.4 on 2024-05-22 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0003_dishtotype_alter_dish_dish_types_delete_dishtype'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='dishtotype',
            unique_together={('dish', 'type')},
        ),
        migrations.AlterUniqueTogether(
            name='measureunit',
            unique_together={('name',), ('short_name',)},
        ),
    ]
