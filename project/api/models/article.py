from django.db import models
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from ..fields import fields


class Article(models.Model):
    title = models.CharField(
        verbose_name=_('Заголовок'),
        max_length=200,
    )
    info = models.CharField(
        verbose_name=_('Информация'),
        max_length=200,
    )
    annotation = models.TextField(
        verbose_name=_('Аннотация'),
        max_length=1024,
    )
    image_url = models.URLField(
        verbose_name=_('Ссылка на изображение'),
        max_length=192,
    )
    color = fields.ColorField(
        verbose_name=_('Цвет'),
        default='#FF0000',
    )
    output_to_main = models.BooleanField(
        verbose_name=_('Отображать на главной странице'),
        default=False,
    )

    def colortile(self):
        if self.color:
            return format_html('<div style="background-color: {0}; \
                height: 100px; width: 100px"></div>', self.color)
        return 'пусто'

    class Meta:
        app_label = 'api'
        ordering = ('id',)
        verbose_name = _('Статья')
        verbose_name_plural = _('Статьи')

    def __str__(self):
        return self.title
