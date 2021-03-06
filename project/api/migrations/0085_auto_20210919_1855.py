# Generated by Django 3.2.3 on 2021-09-19 11:55

import api.validators
from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0084_auto_20210919_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format='JPEG', help_text='Поддерживаемые форматы jpg, jpeg, gif, png, bmp. Размер до 10 Мб.', keep_meta=True, null=True, quality=100, size=[1280, 720], upload_to='articles/', validators=[api.validators.file_size_validator, api.validators.image_extension_validator], verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format='JPEG', help_text='Поддерживаемые форматы jpg, jpeg, gif, png, bmp. Размер до 10 Мб.', keep_meta=True, null=True, quality=100, size=[1280, 720], upload_to='catalog/', validators=[api.validators.file_size_validator, api.validators.image_extension_validator], verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='diary',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format='JPEG', help_text='Поддерживаемые форматы jpg, jpeg, gif, png, bmp. Размер до 10 Мб.', keep_meta=True, null=True, quality=100, size=[1280, 720], upload_to='diaries/', validators=[api.validators.file_size_validator, api.validators.image_extension_validator], verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='history',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format='JPEG', help_text='Поддерживаемые форматы jpg, jpeg, gif, png, bmp. Размер до 10 Мб.', keep_meta=True, null=True, quality=100, size=[1280, 720], upload_to='history/', validators=[api.validators.file_size_validator, api.validators.image_extension_validator], verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format='JPEG', help_text='Поддерживаемые форматы jpg, jpeg, gif, png, bmp. Размер до 10 Мб.', keep_meta=True, null=True, quality=100, size=[1280, 720], upload_to='movies/', validators=[api.validators.file_size_validator, api.validators.image_extension_validator], verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='place',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format='JPEG', help_text='Поддерживаемые форматы jpg, jpeg, gif, png, bmp. Размер до 10 Мб.', keep_meta=True, null=True, quality=100, size=[1280, 720], upload_to='places/', validators=[api.validators.file_size_validator, api.validators.image_extension_validator], verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='video',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format='JPEG', help_text='Поддерживаемые форматы jpg, jpeg, gif, png, bmp. Размер до 10 Мб.', keep_meta=True, null=True, quality=100, size=[1280, 720], upload_to='videos/', validators=[api.validators.file_size_validator, api.validators.image_extension_validator], verbose_name='Изображение'),
        ),
    ]
