# Generated by Django 3.2.3 on 2021-08-10 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0069_remove_right_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rightcontent',
            name='right',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='content', to='api.right', verbose_name='Статья'),
        ),
    ]
