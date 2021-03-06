# Generated by Django 3.2.3 on 2021-06-28 21:24

import api.fields.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0038_alter_movie_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True, verbose_name='Слаг (Ссылка)')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='Название')),
                ('color', api.fields.fields.ColorField(default='#FF0000', max_length=7, verbose_name='Цвет')),
            ],
            options={
                'verbose_name': 'Тип книг',
                'verbose_name_plural': 'Типы книг',
                'ordering': ('name',),
            },
        ),
        migrations.RemoveField(
            model_name='book',
            name='color',
        ),
        migrations.RemoveField(
            model_name='book',
            name='tags',
        ),
        migrations.AddField(
            model_name='book',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='books', to='api.booktype', verbose_name='Тип'),
        ),
    ]
