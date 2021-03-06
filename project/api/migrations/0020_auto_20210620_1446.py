# Generated by Django 3.2.3 on 2021-06-20 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_movie_annotation'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='annotation',
            field=models.TextField(default='Аннотация статьи', max_length=1024, verbose_name='Аннотация'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='image_url',
            field=models.URLField(default='http://server.com/', max_length=192, verbose_name='Ссылка на изображение'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='info',
            field=models.CharField(default='Автор статьи, профессия', max_length=200, verbose_name='Информация'),
            preserve_default=False,
        ),
    ]
