# Generated by Django 5.0.4 on 2024-05-22 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0004_alter_dishtotype_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='is_published',
            field=models.CharField(choices=[('DF', 'Draft'), ('PB', 'Published')], default='DF', max_length=2),
        ),
    ]
