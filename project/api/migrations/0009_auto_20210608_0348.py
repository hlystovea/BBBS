# Generated by Django 3.2.3 on 2021-06-07 20:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_place_activity_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Вид активности')),
            ],
        ),
        migrations.AlterField(
            model_name='place',
            name='activity_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='places', to='api.activitytype', verbose_name='Вид активности'),
        ),
    ]
