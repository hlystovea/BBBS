from django.contrib.auth import get_user_model
from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _


User = get_user_model()


class Diary(models.Model):
    mentor = models.ForeignKey(
        User,
        verbose_name=_('Наставник'),
        on_delete=models.CASCADE,
        related_name='diaries',
    )
    place = models.CharField(
        verbose_name=_('Место встречи'),
        max_length=128,
    )
    date = models.DateField(
        verbose_name=_('Дата'),
        default=now,
    )
    description = models.TextField(
        verbose_name=_('Описание встречи'),
        max_length=1024,
    )
    image_url = models.URLField(
        verbose_name=_('Ссылка на изображение'),
        max_length=192,
        blank=True,
    )
    mark = models.CharField(
        verbose_name=_('Как прошло время'),
        max_length=15,
        choices=(
            ('bad', _('Плохо')),
            ('good', _('Хорошо')),
            ('neutral', _('Нейтрально')),
        ),
    )

    class Meta:
        app_label = 'api'
        ordering = ('-date',)
        verbose_name = _('Дневник')
        verbose_name_plural = _('Дневники')

    def __str__(self):
        return self.place