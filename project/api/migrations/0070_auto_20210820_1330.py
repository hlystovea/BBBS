# Generated by Django 3.2.3 on 2021-08-20 06:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0069_auto_20210819_2009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='url',
        ),
        migrations.AlterField(
            model_name='book',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='books', to='api.booktype', verbose_name='Тип книги'),
        ),
    ]
