# Generated by Django 3.2.3 on 2021-07-13 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0052_merge_0051_catalog_content_0051_video_resource_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='right',
            name='raw_html',
            field=models.TextField(default='<br>', max_length=4000000, verbose_name='HTML'),
            preserve_default=False,
        ),
    ]