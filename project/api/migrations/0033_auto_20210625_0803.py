# Generated by Django 3.2.3 on 2021-06-25 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0032_auto_20210625_0800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='videos/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='video',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='videos/', verbose_name='Изображение'),
        ),
    ]
