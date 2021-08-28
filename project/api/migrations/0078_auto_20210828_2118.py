# Generated by Django 3.2.3 on 2021-08-28 14:18

from django.db import migrations, models
import martor.models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0077_alter_participant_event'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='right',
            name='raw_html',
        ),
        migrations.RemoveField(
            model_name='right',
            name='text',
        ),
        migrations.AddField(
            model_name='right',
            name='body',
            field=martor.models.MartorField(default='Some text', help_text='Основной текст статьи. Для покраски абзаца используйте блок Quote (Ctrl + Q).', verbose_name='Текст статьи'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='movie',
            name='info',
            field=models.CharField(max_length=512, verbose_name='Информация'),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.TextField(blank=True, max_length=2048, null=True, verbose_name='Ответ'),
        ),
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.TextField(max_length=500, verbose_name='Вопрос'),
        ),
        migrations.AlterField(
            model_name='right',
            name='description',
            field=models.TextField(help_text='Отображается над основным текстом статьи.', max_length=1024, verbose_name='Верхний абзац'),
        ),
    ]
