# Generated by Django 3.2.3 on 2021-07-17 21:25

from django.db import migrations, models
import django.db.models.functions.datetime


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0062_auto_20210717_0033'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='book',
            index=models.Index(fields=['type'], name='book_type_slug_index'),
        ),
        migrations.AddIndex(
            model_name='event',
            index=models.Index(django.db.models.functions.datetime.Extract('start_at', 'month'), name='event_start_at_month_index'),
        ),
        migrations.AddIndex(
            model_name='event',
            index=models.Index(django.db.models.functions.datetime.Extract('start_at', 'year'), name='event_start_at_year_index'),
        ),
        migrations.AddIndex(
            model_name='place',
            index=models.Index(fields=['moderation_flag', 'city'], name='api_place_moderat_fd91ee_idx'),
        ),
    ]
