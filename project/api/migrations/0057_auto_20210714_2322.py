# Generated by Django 3.2.3 on 2021-07-14 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0056_auto_20210714_2045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catalog',
            name='content',
        ),
        migrations.AddField(
            model_name='catalog',
            name='raw_html',
            field=models.TextField(default='<br>', max_length=4000000, verbose_name='HTML'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='history',
            name='raw_html',
            field=models.TextField(default='<br>', max_length=4000000, verbose_name='HTML'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='tags',
            field=models.ForeignKey(limit_choices_to={'category': 'События'}, on_delete=django.db.models.deletion.PROTECT, related_name='events', to='api.tag', verbose_name='Тег(и)'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='tags',
            field=models.ManyToManyField(limit_choices_to={'category': 'Фильмы'}, related_name='movies', to='api.Tag', verbose_name='Теги'),
        ),
        migrations.AlterField(
            model_name='place',
            name='tags',
            field=models.ManyToManyField(limit_choices_to={'category': 'Места'}, related_name='places', to='api.Tag', verbose_name='Тег(и)'),
        ),
        migrations.AlterField(
            model_name='question',
            name='tags',
            field=models.ManyToManyField(limit_choices_to={'category': 'Вопросы'}, related_name='questions', to='api.Tag', verbose_name='Тег(и)'),
        ),
        migrations.AlterField(
            model_name='right',
            name='tags',
            field=models.ManyToManyField(limit_choices_to={'category': 'Права'}, related_name='rights', to='api.Tag', verbose_name='Тег(и)'),
        ),
        migrations.AlterField(
            model_name='video',
            name='tags',
            field=models.ManyToManyField(limit_choices_to={'category': 'Видеоролики'}, related_name='videos', to='api.Tag', verbose_name='Теги'),
        ),
    ]
