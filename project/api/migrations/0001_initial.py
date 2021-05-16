# Generated by Django 3.2.3 on 2021-05-15 15:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(128)], verbose_name='Заголовок')),
                ('info', models.TextField(max_length=512, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(512)], verbose_name='Информация')),
                ('image_url', models.URLField(max_length=192, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(192)], verbose_name='Ссылка на изображение')),
                ('link', models.URLField(max_length=192, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(192)], verbose_name='Ссылка на фильм')),
            ],
            options={
                'verbose_name': 'Фильм',
                'verbose_name_plural': 'Фильмы',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(128)], verbose_name='Заголовок')),
                ('info', models.TextField(max_length=512, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(512)], verbose_name='Информация')),
                ('image_url', models.URLField(max_length=192, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(192)], verbose_name='Ссылка на изображение')),
                ('link', models.URLField(max_length=192, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(192)], verbose_name='Ссылка на видеоролик')),
            ],
            options={
                'verbose_name': 'Видеоролик',
                'verbose_name_plural': 'Видеоролики',
            },
        ),
    ]