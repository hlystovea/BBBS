# Generated by Django 3.2.3 on 2021-06-23 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0027_auto_20210622_2310'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='videos/'),
        ),
        migrations.AlterField(
            model_name='video',
            name='image_url',
            field=models.URLField(blank=True, max_length=192, null=True, verbose_name='Ссылка на изображение'),
        ),
    ]
