# Generated by Django 3.2.3 on 2021-07-15 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0057_auto_20210714_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='age_restriction',
            field=models.CharField(choices=[('8-10', '8-10'), ('11-13', '11-13'), ('14-17', '14-17'), ('18', '18+'), ('any', 'Любой')], max_length=50, verbose_name='Целевой возраст'),
        ),
    ]