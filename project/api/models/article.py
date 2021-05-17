from django.db import models
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from ..fields import fields


class Article(models.Model):
    title = models.CharField(
        verbose_name=_('Заголовок'),
        max_length=200,
    )
    color = fields.ColorField(
        verbose_name=_('Цвет'),
        default='#FF0000')

    def colortile(self):
        if self.color:
            return format_html('<div style="background-color: {0}; \
                height: 100px; width: 100px"></div>', self.color)
        return 'пусто'

    class Meta:
        app_label = 'api'

    def __str__(self):
        return self.title
