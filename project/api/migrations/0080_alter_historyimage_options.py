# Generated by Django 3.2.3 on 2021-08-28 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0079_auto_20210828_2249'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historyimage',
            options={'ordering': ('order',), 'verbose_name': 'Изображение в слайдере', 'verbose_name_plural': 'Изображения в слайдере'},
        ),
    ]
