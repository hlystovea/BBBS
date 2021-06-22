# Generated by Django 3.2.3 on 2021-06-20 13:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0023_diary'),
    ]

    operations = [
        migrations.AddField(
            model_name='diary',
            name='mentor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='diaries', to='account.customuser', verbose_name='Наставник'),
            preserve_default=False,
        ),
    ]
