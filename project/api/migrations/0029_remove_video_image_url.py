# Generated by Django 3.2.3 on 2021-06-23 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0028_auto_20210623_1758'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='image_url',
        ),
    ]
