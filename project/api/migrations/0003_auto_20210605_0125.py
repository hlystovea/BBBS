# Generated by Django 3.2.3 on 2021-06-04 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210605_0118'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='address',
            field=models.CharField(default='', max_length=200, verbose_name='Адрес'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='place',
            name='output_to_main',
            field=models.BooleanField(default=False, verbose_name='Отображать на главной странице'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='place',
            name='chosen',
            field=models.BooleanField(default=False, verbose_name='Выбор наставника'),
        ),
    ]
