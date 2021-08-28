# Generated by Django 3.2.3 on 2021-08-28 15:49

import common.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(help_text='Поддерживаемые форматы jpg, jpeg, gif, png, bmp. Размер до 10 Мб.', upload_to='images/', validators=[common.validators.file_size_validator, common.validators.image_extension_validator], verbose_name='Изображение')),
                ('image_caption', models.CharField(max_length=200, verbose_name='Подпись к изображению')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
            },
        ),
    ]
