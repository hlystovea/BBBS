# Generated by Django 3.2.3 on 2021-07-14 13:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0054_alter_catalog_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='blocking_view',
            field=models.BooleanField(default=True, verbose_name='Заблокировать отображение на сайте'),
        ),
        migrations.AlterField(
            model_name='video',
            name='duration',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(86400)], verbose_name='Продолжительность видеоролика в сек.'),
        ),
    ]
