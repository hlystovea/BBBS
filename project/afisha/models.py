from django.db import models
from django.utils.translation import gettext_lazy as _


class EventMailing(models.Model):
    event = models.ForeignKey(
        'api.Event',
        verbose_name=_('Событие'),
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        'api.Event',
        on_delete=models.CASCADE,
        verbose_name=_('Пользователь')
    )
    date_sending = models.DateTimeField(
        verbose_name=_('Время отправки'),
        auto_now_add=True,
    )
    mailing_type = models.CharField(
        verbose_name=_('Тип отправки'),
        max_length=12,
        choices=(
            ('cancellation', _('Отмена')),
            ('reminder', _('Напоминание'))
        ),
    )

    class Meta:
        ordering = ('-date_sending',)
        verbose_name = _('Рассылка отмены события')
        verbose_name_plural = _('Рассылки отмены событий')
