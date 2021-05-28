from django.db import models
from django.utils.translation import gettext_lazy as _


class Movie(models.Model):
    title = models.CharField(
        verbose_name=_('Заголовок'),
        max_length=128,
    )
    info = models.TextField(
        verbose_name=_('Информация'),
        max_length=512,
    )
    image_url = models.URLField(
        verbose_name=_('Ссылка на изображение'),
        max_length=192,
    )
    link = models.URLField(
        verbose_name=_('Ссылка на фильм'),
        max_length=192,
    )
    tags = models.ManyToManyField(
        'api.Tag',
        verbose_name=_('Тег(и)'),
        related_name='movies',
        blank=True
    )

    class Meta:
        app_label = 'api'
        ordering = ('id',)
        verbose_name = _('Фильм')
        verbose_name_plural = _('Фильмы')

    def __str__(self):
        return self.title
