# Generated by Django 3.2.3 on 2021-09-04 14:37

import api.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0080_alter_historyimage_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ('category', 'order'), 'verbose_name': 'Тег', 'verbose_name_plural': 'Теги'},
        ),
        migrations.AddField(
            model_name='tag',
            name='order',
            field=models.PositiveSmallIntegerField(default=0, help_text='Теги с меньшим значением выводятся первыми.', verbose_name='Порядок вывода'),
        ),
        migrations.AlterField(
            model_name='place',
            name='image',
            field=models.ImageField(blank=True, help_text='Поддерживаемые форматы jpg, jpeg, gif, png, bmp. Размер до 10 Мб.', null=True, upload_to='places/', validators=[api.validators.file_size_validator, api.validators.image_extension_validator], verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='place',
            name='image_url',
            field=models.URLField(blank=True, help_text='Альтернативный способ загрузки изображения. Приоритет у файла.', null=True, verbose_name='Ссылка на изображение'),
        ),
    ]
