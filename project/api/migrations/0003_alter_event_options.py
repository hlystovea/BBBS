# Generated by Django 3.2.3 on 2021-06-01 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_main_events'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ('-start_at',), 'permissions': (('events_in_all_cities', 'Можно смотреть события всех городов'),), 'verbose_name': 'Событие', 'verbose_name_plural': 'События'},
        ),
    ]
